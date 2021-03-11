import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_asesoria, update_asesoria, delete_encuesta
from rest_api_si_empre.api.roles.serializers import asesorias
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_asesorias, Tbl_estudiantes, tbl_encuesta, tbl_usuario, tbl_estado
from sqlalchemy import exc
import sqlalchemy
from rest_api_si_empre.database import db

log = logging.getLogger(__name__)

ns = api.namespace('roles/asesorias', description='Operaciones permitidas en asesorias')

@ns.route('/')
class AsesoriasCollection(Resource):
    
    @api.marshal_with(asesorias)
    def get(self):
        """
        Lista de asesorias, hecha para vista administrador
        """
        asesorias = tbl_asesorias.query.all()        
        if asesorias:            
            return asesorias
        else: 
            asesorias_one = tbl_asesorias.query.first()
            if asesorias_one:
                return asesorias_one
            else:
                asesorias = {}
                return None, 404
    
    @api.expect(asesorias)
    def post(self):
        """
        Creates a new asesoria
        """        
        status = create_asesoria(request.json)
        if status != None:
            return "{'status':'No se pudo guardar el registro, consulte con el admin del sistema'}", 404            
        else:
            return "{'status':'Registro guardado'}", 201



@ns.route('/<int:id>')
@api.response(404, 'Asesorias not found.')
class Asesorias(Resource):

    @api.marshal_with(asesorias)
    def get(self, id):
        """
        Returns a asesorias
        """
        return tbl_asesorias.query.filter(tbl_asesorias.id == id).one()

    @api.expect(asesorias)
    @api.response(204, 'Asesorias successfully updated.')
    def put(self, id):
        """
        Updates a Asesorias
        """
        data = request.json 
        status = update_asesoria(id, data)
        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'registro con incovenientes'}", 403

    @api.response(204, 'Encuesta sucecessfully validated') 
    def delete(self, id):
        """
        Deletes encuestas
        """
        delete_encuesta(id)
        return None, 204


# Asesorias Totales Para ser Auditadas    
@ns.route('/asesor')
@api.response(404, 'Asesorias estudiantes')
class AsesoriasAdmin(Resource):
    
    def get(self):
        """
        Returns todos los estdudiantes para ser validados por admin
        """  
        aux = 0
        list_final_asesoria = {}
        encuestas = tbl_encuesta.query.filter((tbl_encuesta.estado_id == 3) | (tbl_encuesta.estado_id == 4)).all()
        if encuestas: 
            list_asesorias = []
            for encuesta in encuestas:
                dict_encuesta = {}       
                dict_encuesta['id_encuesta'] = encuesta.id
                dict_encuesta['validacion'] = encuesta.validacion
                # dict_encuesta['id_estado'] = encuesta.estado_id
                dict_encuesta['observacion'] = encuesta.observacion
                dict_encuesta['id_asesoria'] = encuesta.asesorias_id                
                asesoria = tbl_asesorias.query.filter(tbl_asesorias.id == encuesta.asesorias_id).one()                   
                empresario = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_estudiante).one()
                empresa = Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == empresario.id).one()
                estado = tbl_estado.query.filter(tbl_estado.id == encuesta.estado_id).one()
                dict_encuesta['estado'] = estado.estado
                dict_encuesta['nombre_empresario'] = empresario.nombre
                dict_encuesta['apellido_empresario'] = empresario.apellido
                dict_encuesta['telefono_empresario'] = empresario.telefono
                dict_encuesta['email_empresario'] = empresario.email
                dict_encuesta['nombre_empresa'] = empresa.empresa
                asesor = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_asesor).one()
                dict_encuesta['nombre_asesor'] = asesor.nombre
                dict_encuesta['apellido_asesor'] = asesor.apellido
                dict_encuesta['telefono_asesor'] = asesor.telefono
                dict_encuesta['email_asesor'] = asesor.email
                list_asesorias.append(dict_encuesta)
            return list_asesorias  
        else:
            encuesta = tbl_encuesta.query.filter((tbl_encuesta.estado_id == 3) | (tbl_encuesta.estado_id == 4)).one()
            if encuesta:
                list_asesorias = []            
                dict_encuesta = {}       
                dict_encuesta['id_encuesta'] = encuesta.id
                dict_encuesta['validacion'] = encuesta.validacion
                # dict_encuesta['id_estado'] = encuesta.estado_id
                dict_encuesta['observacion'] = encuesta.observacion
                dict_encuesta['id_asesoria'] = encuesta.asesorias_id                
                asesoria = tbl_asesorias.query.filter(tbl_asesorias.id == encuesta.asesorias_id).one()                   
                empresario = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_estudiante).one()
                empresa = Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == empresario.id).one()
                estado = tbl_estado.query.filter(tbl_estado.id == encuesta.estado_id).one()
                dict_encuesta['estado'] = estado.estado
                dict_encuesta['nombre_empresario'] = empresario.nombre
                dict_encuesta['apellido_empresario'] = empresario.apellido
                dict_encuesta['telefono_empresario'] = empresario.telefono
                dict_encuesta['email_empresario'] = empresario.email
                dict_encuesta['nombre_empresa'] = empresa.empresa
                asesor = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_asesor).one()
                dict_encuesta['nombre_asesor'] = asesor.nombre
                dict_encuesta['apellido_asesor'] = asesor.apellido
                dict_encuesta['telefono_asesor'] = asesor.telefono
                dict_encuesta['email_asesor'] = asesor.email
                list_asesorias.append(dict_encuesta)
                return list_asesorias              
            else:
                asesorias = {}
                return asesorias, 404 
    
    def post(self):
        """
        Notificar asesor y cambiar estao de encuesta a 1
        """
        data = request.json
        id_encuesta = data.get('id_encuesta')
        encuesta = tbl_encuesta.query.filter(tbl_encuesta.id == id_encuesta).one()        
        if encuesta:
            estado = tbl_estado.query.filter(tbl_estado.id == 1).one()
            encuesta.estado_id = estado.id            
            db.session.add(encuesta)
            db.session.commit()
            response = getDataEmail(encuesta.asesorias_id)
            if response != 0:
                return response, 201
            else:
                return 403
        else:
            data = {'error': 'No existe encuesta', 'status': 404}
            return data, 404


def getDataEmail(id_asesoria):
    dict_asesor = {}
    asesoria = tbl_asesorias.query.filter(tbl_asesorias.id == id_asesoria).one()
    if asesoria:
        id_asesor = asesoria.id_asesor
        print(id_asesor)
        id_estudiante = asesoria.id_estudiante
        asesor = tbl_usuario.query.filter(tbl_usuario.id == id_asesor).one()
        dict_asesor['nombre_asesor'] = asesor.nombre
        dict_asesor['apellido_asesor'] = asesor.apellido
        dict_asesor['email_asesor'] = asesor.email
        estudiante = tbl_usuario.query.filter(tbl_usuario.id == id_estudiante).one()
        dict_asesor['nombre_estudiante'] = estudiante.nombre
        dict_asesor['apellido_estudiante'] = estudiante.apellido
        dict_asesor['email_estudiante'] = estudiante.email
        dict_asesor['telefono'] = estudiante.telefono
        return dict_asesor
    return 0



@ns.route('/asesor/<int:id_asesor>')
@api.response(404, 'estudiantes filtrado por asesor')
class AsesoriasItem(Resource):
    
    def get(self, id_asesor):
        """
        Returns todos los estduiantes filtrado por asesor
        """  
        aux = 0
        list_final_asesoria = {}
        asesorias = tbl_asesorias.query.filter(tbl_asesorias.id_asesor == id_asesor).all()
        if asesorias: 
            list_asesorias = []
            for asesoria in asesorias:
                dict_asesoria = {}        
                dict_asesoria['id'] = asesoria.id
                dict_asesoria['id_estudiante'] = asesoria.id_estudiante
                usuario = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_estudiante).one()
                estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == asesoria.id_estudiante).one()                
                dict_asesoria['estudiante_empresa'] = estudiante.empresa 
                dict_asesoria['estudiante_id_subsector'] = estudiante.id_subsector 
                dict_asesoria['estudiante_per_emp'] = estudiante.per_emp
                dict_asesoria['estudiante_actividad_e'] = estudiante.actividad_e
                dict_asesoria['estudiante_direccion_e'] = estudiante.direccion_e
                dict_asesoria['estudiante_barrio_e'] = estudiante.barrio_e
                # nuevos campos
                dict_asesoria['estudiante_facebook'] = estudiante.facebook
                dict_asesoria['estudiante_instagram'] = estudiante.instagram
                dict_asesoria['estudiante_num_whatsapp'] = estudiante.num_whatsapp
                dict_asesoria['estudiante_num_emp'] = estudiante.num_emp
                dict_asesoria['estudiante_ano_fun'] = estudiante.ano_fun
                dict_asesoria['estudiante_telefono'] = usuario.telefono
                # Termina nuevos campos
                dict_asesoria['estudiante_nombre'] = usuario.nombre
                dict_asesoria['estudiante_apellido'] = usuario.apellido
                dict_asesoria['id_asesor'] = asesoria.id_asesor
                asesor = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_asesor).one()
                dict_asesoria['asesor_nombre'] = asesor.nombre
                dict_asesoria['asesor_apellido'] = asesor.apellido
                try:
                    encuesta = tbl_encuesta.query.filter(tbl_encuesta.asesorias_id == asesoria.id).one()                   
                    dict_asesoria['estado_encuesta'] = encuesta.estado_id                        
                except sqlalchemy.orm.exc.NoResultFound:
                    dict_asesoria['estado_encuesta'] = 1                
                list_asesorias.append(dict_asesoria)
            list_final_asesoria['asesorias'] = list_asesorias
            contador = contarTerminadas(list_asesorias)
            porcen = porcentaje(contador, len(asesorias))
            list_final_asesoria['porcentaje'] = porcen            
            return list_final_asesoria
        else: 
            asesorias_one = tbl_asesorias.query.filter(tbl_asesorias.id_asesor == id_asesor).first()
            if asesorias_one:
                list_asesorias = []
                for asesoria in asesorias:
                    dict_asesoria = {}        
                    dict_asesoria['id'] = asesoria.id
                    dict_asesoria['id_estudiante'] = asesoria.id_estudiante
                    usuario = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_estudiante).one()
                    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == asesoria.id_estudiante).one()                   
                    dict_asesoria['estudiante_empresa'] = estudiante.empresa 
                    dict_asesoria['estudiante_id_subsector'] = estudiante.id_subsector 
                    dict_asesoria['estudiante_per_emp'] = estudiante.per_emp 
                    dict_asesoria['estudiante_actividad_e'] = estudiante.actividad_e
                    dict_asesoria['estudiante_direccion_e'] = estudiante.direccion_e
                    dict_asesoria['estudiante_barrio_e'] = estudiante.barrio_e
                    dict_asesoria['estudiante_facebook'] = estudiante.facebook
                    dict_asesoria['estudiante_instagram'] = estudiante.instagram
                    dict_asesoria['estudiante_num_whatsapp'] = estudiante.num_whatsapp
                    dict_asesoria['estudiante_num_emp'] = estudiante.num_emp
                    dict_asesoria['estudiante_ano_fun'] = estudiante.ano_fun
                    dict_asesoria['estudiante_telefono'] = usuario.telefono
                    dict_asesoria['estudiante_nombre'] = usuario.nombre
                    dict_asesoria['estudiante_apellido'] = usuario.apellido                    
                    dict_asesoria['id_asesor'] = asesoria.id_asesor
                    asesor = tbl_usuario.query.filter(tbl_usuario.id == asesoria.id_asesor).one()
                    dict_asesoria['asesor_nombre'] = asesor.nombre
                    dict_asesoria['asesor_apellido'] = asesor.apellido
                    try:
                        encuesta = tbl_encuesta.query.filter(tbl_encuesta.asesorias_id == asesoria.id).one()
                        dict_asesoria['estado_encuesta'] = encuesta.estado_id                        
                    except sqlalchemy.orm.exc.NoResultFound:
                        dict_asesoria['estado_encuesta'] = 1                                           
                    list_asesorias.append(dict_asesoria)
                list_final_asesoria['asesorias'] = list_asesorias
                contador = contarTerminadas(list_asesorias)
                porcen = porcentaje(contador, len(asesorias_one))
                list_final_asesoria['porcentaje'] = porcen                 
                return list_final_asesoria
            else:
                asesorias = {}
                return asesorias, 404


def contarTerminadas(encuestas):
    aux = 0
    for contador in encuestas:
        if contador['estado_encuesta'] == 3:
            aux = aux + 1
    return aux


def porcentaje(terminadas, asignadas):
    terminadas = terminadas * 100
    porcentaje = terminadas//asignadas
    return porcentaje



@ns.route('/confirmar-datos')
@api.response(404, 'Asesorias not found.')
class AsesoriasConfirmarDatos(Resource):

    @api.response(204, 'Confirmar datos de estudiante')
    def put(self):
        """
        Confirmar datos estudiante
        """
        data = request.json 
        id = data.get('id')
        actividad_e = data.get('actividad_e')
        direccion_e = data.get('direccion_e')
        barrio_e = data.get('barrio_e')
        num_whatsapp = data.get('num_whatsapp')
        facebook = data.get('facebook')
        instagram = data.get('instagram')
        num_emp = data.get('num_emp')
        ano_fun = data.get('ano_fun')
        id_subsector = data.get('id_subsector')
        per_emp = data.get('per_emp')
        empresa = data.get('empresa')
        estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == id).one()
        if estudiante:           
            estudiante.actividad_e = actividad_e
            estudiante.direccion_e = direccion_e
            estudiante.barrio_e = barrio_e
            estudiante.num_whatsapp = num_whatsapp
            estudiante.facebook = facebook
            estudiante.instagram = instagram
            estudiante.num_emp = num_emp
            estudiante.ano_fun = ano_fun
            estudiante.id_subsector = id_subsector
            estudiante.per_emp = per_emp
            estudiante.empresa = empresa
            db.session.add(estudiante)
            db.session.commit()            
            return 200
        else:
            return 404               