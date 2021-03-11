import logging
from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_programacion, update_programacion, delete_programacion
from rest_api_si_empre.api.roles.serializers import programacion, page_of_programacion
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_programacion, Tbl_grupo, tbl_curso, Tbl_franja

log = logging.getLogger(__name__)

ns = api.namespace('roles/programacion', description='Operaciones permitidas en programacion')


@ns.route('/')
class ProgramacionCollection(Resource):
    
    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_programacion)
    def get(self):
        """
        Returns list of roles.
        """   

        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        programacion_query = Tbl_programacion.query
        Tbl_programacion_page = programacion_query.paginate(page, per_page, error_out=False)
                
        return Tbl_programacion_page

    
    @api.expect(programacion)
    def post(self):
        """
        Creates a new programacion.
        """
        create_programacion(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Curso not found.')
class ProgramacionItem(Resource):

    @api.marshal_with(programacion)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return Tbl_programacion.query.filter(Tbl_programacion.id == id).one()

    @api.expect(programacion)
    @api.response(204, 'Programacion successfully updated.')
    def put(self, id):
        """
        Updates a programacion
        """
        data = request.json
        status = update_programacion(id, data)

        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'Registro no guardado'}", 403
        

    @api.response(204, 'Programacion successfully deleted.')
    def delete(self, id):
        """
        Deletes curso.
        """
        delete_programacion(id)
        return None, 204

@ns.route('/grupo/<int:id>')
@api.response(404, 'Curso not found.')
class Programacion_grupo_Item(Resource):

    @api.marshal_with(programacion)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return Tbl_programacion.query.filter(Tbl_grupo.id == id).all()



@ns.route('/profesor/<int:id_curso_profesor>')
@api.response(404, 'Curso not found.')
class Programacion_profesor_Item(Resource):

    @api.marshal_with(programacion)
    def get(self, id_curso_profesor):
        """
        Returns a estudiantes
        """
        return Tbl_programacion.query.filter(Tbl_programacion.id_curso == id_curso_profesor).all()



@ns.route('/grupo_franja_cursos')
class Programacion_grupo_franja_cursos_Collection(Resource):

    def get(self):
        """
        Returns list of grupos, franja y cursos.
        """         
        listado = {}
        franjas = Tbl_franja.query.all()        
        lista_franjas = []
        for item in franjas:
            dict_franja = {}      
            dict_franja['id'] = item.id
            dict_franja['nombre'] = item.nombre
            lista_franjas.append(dict_franja)
        listado['franjas'] = lista_franjas
        grupos = Tbl_grupo.query.all()
        listado_grupo = []
        for item in grupos:
            dict_grupos = {}
            dict_grupos['id'] = item.id
            dict_grupos['descripcion'] = item.descripcion
            listado_grupo.append(dict_grupos)
        listado['grupos'] = listado_grupo        
        cursos = tbl_curso.query.all()
        listado_curso = []
        for item in cursos:
            dict_cursos = {}
            dict_cursos['id'] = item.id
            dict_cursos['titulo'] = item.titulo
            dict_cursos['descripcion'] = item.descripcion
            listado_curso.append(dict_cursos)
        listado['cursos'] = listado_curso        
        return listado