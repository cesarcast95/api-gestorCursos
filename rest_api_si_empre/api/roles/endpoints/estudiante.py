import logging
import json

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_estudiante, update_estudiante, delete_estudiante
from rest_api_si_empre.api.roles.serializers import estudiante, page_of_estudiante
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_estudiantes, Tbl_grupo, tbl_curso, tbl_usuario, tbl_curso_profesor
from rest_api_si_empre.database.models import Tbl_monitorias
from rest_api_si_empre.database import db


log = logging.getLogger(__name__)

ns = api.namespace('roles/estudiante', description='Operaciones permitidas en estudiantes')


@ns.route('/')
class EstudiantesCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_estudiante)
    def get(self):
        """
        Returns list of estudiantes.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        estudiante_query = Tbl_estudiantes.query
        tbl_estudiantes_page = estudiante_query.paginate(page, per_page, error_out=False)

        return tbl_estudiantes_page

    
    @api.expect(estudiante)
    def post(self):
        """
        Creates a new Estudiante.
        """
        status = create_estudiante(request.json)        
        if status == 201:
            return "{'status':'Registro guardado'}", 201
        else:
            return "{'status':'Solo puedes ingresar 10000 registros'}", 403        


@ns.route('/<int:id>')
@api.response(404, 'Estudiantes not found.')
class EstudiantesGrupoCurso(Resource):

    @api.marshal_with(estudiante)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id).one()

    @api.expect(estudiante)
    @api.response(204, 'Estudiante successfully updated.')
    def put(self, id):
        """
        Updates a Estudiante
        """
        data = request.json
        status = update_estudiante(id, data)
        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'registro con incovenientes'}", 403

    @api.response(204, 'Estudiante successfully deleted.')
    def delete(self, id):
        """
        Deletes estudiante.
        """
        delete_estudiante(id)
        return None, 204

@ns.route('/usuario/<int:id>')
@api.response(404, 'Usuario not found.')
class UsuarioItem(Resource):

    @api.marshal_with(estudiante)
    def get(self, id):
        """
        Returns a Usuarios
        """
        return Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == id).all()


@ns.route('/cursos-grupos')
class EstudiantesCollection(Resource):

    def get(self):
        """
        Returns list of estudiantes, grupos y cursos.
        """         
        listado = {}
        usuarios = tbl_usuario.query.all()
        lista_usuarios = []
        for item in usuarios:
            dict_usuario = {}
            dict_usuario['id'] = item.id
            dict_usuario['nombre'] = item.nombre
            dict_usuario['apellido'] = item.apellido            
            dict_usuario['identificacion'] = item.identificacion
            lista_usuarios.append(dict_usuario)
        listado['usuarios'] = lista_usuarios
        estudiantes = Tbl_estudiantes.query.all()            
        lista_estudiantes = []
        for item in estudiantes:          
            dict_estudiante = {}      
            dict_estudiante['id'] = item.id        
            dict_estudiante['nombre'] = '{nombre} {apellido}'.format(nombre=item.usuario.nombre, apellido=item.usuario.apellido)                  
            lista_estudiantes.append(dict_estudiante)
        listado['estudiantes'] = lista_estudiantes          
        grupos = Tbl_grupo.query.all()
        listado_grupo = []        
        for item in grupos:            
            dict_grupos = {}
            dict_grupos['id'] = item.id
            dict_grupos['descripcion'] = item.descripcion
            listado_grupo.append(dict_grupos)
        listado['grupos'] = listado_grupo           
        cursos = tbl_curso_profesor.query.all()
        listado_curso = []
        for item in cursos:
            dict_cursos = {}
            dict_cursos['id'] = item.id
            dict_cursos['titulo'] = item.curso.titulo            
            dict_cursos['profesor'] = '{nombre} {apellido}'.format(nombre=item.profesor.nombre, apellido=item.profesor.apellido)
            dict_cursos['salon'] = item.grupo.descripcion
            listado_curso.append(dict_cursos)
        listado['cursos'] = listado_curso         
        return listado


@ns.route('/all')
@api.response(404, 'Group not found.')
class GroupItemAll(Resource):

    @api.marshal_with(estudiante)
    def get(self):
        """
        Returns a group with a list of posts.
        """
        return Tbl_estudiantes.query.all()


@ns.route('/monitor/<int:id>')
@api.response(404, 'Monitoria not found.')
class EstudianteMonitor(Resource):
    
    def get(self, id):
        """
        Returns a group with a list of posts.
        """
        list_monitorias = []
        monitorias = Tbl_monitorias.query.filter(Tbl_monitorias.id_monitor == id).all()
        if monitorias:
            print('muchos###')
            for monitoria in monitorias:
                dict_monitoria = {}
                estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == monitoria.id_estudiante).one()
                dict_monitoria['empresa'] = estudiante.empresa   
                usuario = tbl_usuario.query.filter(tbl_usuario.id == estudiante.id_usuario).one()
                dict_monitoria['id'] = estudiante.id
                dict_monitoria['nombre'] = usuario.nombre
                dict_monitoria['apellido'] = usuario.apellido
                list_monitorias.append(dict_monitoria)
            return list_monitorias
        else:
            print('uno solamente###')
            monitoria = Tbl_monitorias.query.filter(Tbl_monitorias.id_monitor == id).all()
            if monitoria:            
                dict_monitoria = {}
                estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == monitoria.id_estudiante).one()                
                dict_monitoria['empresa'] = estudiante.empresa  
                usuario = tbl_usuario.query.filter(tbl_usuario.id == estudiante.id_usuario).one()
                dict_monitoria['id'] = estudiante.id
                dict_monitoria['nombre'] = usuario.nombre
                dict_monitoria['apellido'] = usuario.apellido
                list_monitorias.append(dict_monitoria)
            return list_monitorias
        return 404



@ns.route('/ubicacion')
@api.response(404, 'Group not found.')
class GroupItemAll(Resource):
    
    def post(self):
        """
        Actualizar ubicacion del empresario.
        """

        data = request.json
        print(data['id'], data['latitud'], data['longitud'])
        latitud = data['latitud'].replace(',', '.')
        longitud = data['longitud'].replace(',', '.')
        estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == data['id']).one()
        estudiante.latitud = float(latitud)
        estudiante.longitud = float(longitud)
        # nuevos campos
        estudiante.direccion_e = data['direccion_e']
        estudiante.barrio_e = data['barrio_e']
        estudiante.comuna_e = data['comuna_e']
        db.session.add(estudiante)
        db.session.commit()

        usuario = tbl_usuario.query.filter(tbl_usuario.id == data['id_usuario']).one()
        usuario.identificacion = data['identificacion']
        db.session.add(usuario)
        db.session.commit()
        return 200




@ns.route('/all-estudiantes/geovisor')
@api.response(404, 'Group not found.')
class EstudiantesGeovisor(Resource):
    
    def get(self):
        """
        Returns estudiantes para geovisor.
        """
        estudiantes_list = []
        estudiantes_all = Tbl_estudiantes.query.filter(Tbl_estudiantes.latitud != 0, Tbl_estudiantes.activo == True).all()
        if estudiantes_all:
            print('entra aqui all')
            for estudiante in estudiantes_all:
                estudiante_dict = {}
                estudiante_dict['id'] = estudiante.id
                estudiante_dict['longitud'] = estudiante.longitud
                estudiante_dict['latitud'] = estudiante.latitud
                estudiante_dict['empresa'] = estudiante.empresa
                estudiante_dict['id_subsector'] = estudiante.id_subsector
                estudiante_dict['subsector'] = estudiante.subsector.nombre
                estudiante_dict['direccion_e'] = estudiante.direccion_e
                estudiante_dict['barrio_e'] = estudiante.barrio_e
                estudiante_dict['num_whatsapp'] = estudiante.num_whatsapp
                estudiantes_list.append(estudiante_dict)                
        else:
            estudiantes_one = Tbl_estudiantes.query.filter(Tbl_estudiantes.latitud != 0, Tbl_estudiantes.activo == True).first()
            print('entra aqui one')
            if estudiantes_one:
                for estudiante in estudiantes_one:
                    estudiante_dict = {}
                    estudiante_dict['id'] = estudiante.id
                    estudiante_dict['longitud'] = estudiante.longitud
                    estudiante_dict['latitud'] = estudiante.latitud
                    estudiante_dict['empresa'] = estudiante.empresa
                    estudiante_dict['id_subsector'] = estudiante.id_subsector
                    estudiante_dict['subsector'] = estudiante.subsector.nombre
                    estudiante_dict['direccion_e'] = estudiante.direccion_e
                    estudiante_dict['barrio_e'] = estudiante.barrio_e
                    estudiantes_list.append(estudiante_dict)
            else:
                # aqui devuelve 
                response = {
                    'estado': 404
                }
                estudiantes_list.append(response)
        return estudiantes_list
