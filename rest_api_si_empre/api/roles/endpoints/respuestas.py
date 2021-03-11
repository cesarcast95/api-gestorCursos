import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_respuesta, update_respuesta
from rest_api_si_empre.api.roles.serializers import respuestas
from rest_api_si_empre.api.restplus import api
from datetime import datetime
from rest_api_si_empre.database import db
from rest_api_si_empre.database.models import tbl_respuestas, tbl_preguntas, tbl_encuesta, tbl_estado, tbl_calificacion
from sqlalchemy import exc

log = logging.getLogger(__name__)

ns = api.namespace('roles/respuestas', description='Operaciones permitidas en respuestas')

@ns.route('/')
class RespuestasCollection(Resource):
    
    @api.marshal_with(respuestas)
    def get(self):
        """
        Lista de respuestas, hecha para vista administrador
        """        
        respuestas = tbl_respuestas.query.all()        
        if respuestas:            
            return respuestas
        else: 
            respuestas_one = tbl_respuestas.query.first()
            if respuestas_one:
                return respuestas_one
            else:
                respuestas = {}
                return None, 404
    

    @api.expect(respuestas)
    def post(self):
        """
        Creates a new respuestas
        """   
        data = request.json
        encuesta_id = int(data['encuesta_id'])               
        data = create_respuesta(data)
        num_respuestas = tbl_respuestas.query.filter(tbl_respuestas.encuesta_id == encuesta_id).all()                                                                 
        if len(num_respuestas) > 29:
                encuesta = tbl_encuesta.query.filter(tbl_encuesta.id == encuesta_id).one()
                encuesta.estado = tbl_estado.query.filter(tbl_estado.id == 3).one()              
                encuesta.fecha_actualizacion = datetime.utcnow()
                db.session.add(encuesta)
                db.session.commit()
                return "{'status':'Numero de respuestas completo, Encuesta terminada'}", 403      
        if data != None:
            return "{'status':'No se pudo guardar el registro, consulte con el admin del sistema'}", 404          
        else:
            return "{'status':'Registro guardado'}", 201



@ns.route('/<int:encuesta_id>')
@api.response(404, 'Respuestas not found.')
class Respuestas(Resource):
    """
    Endpoint para ver la respuesta por su id
    """

    @api.marshal_with(respuestas)
    def get(self, encuesta_id):
        """
        Returns a asesorias
        """
        respuestas = tbl_respuestas.query.filter(tbl_respuestas.encuesta_id == encuesta_id).all()        
        if respuestas:   
            return respuestas, 200
        else: 
            respuestas_one = tbl_respuestas.query.filter(tbl_respuestas.encuesta_id == encuesta_id).first()
            if respuestas_one:
                return respuestas_one, 200
            else:
                respuestas = {
                    'status': '400',
                    'mensaje': 'No existen respuestas'
                }
                return respuestas, 404
                
                        

    @api.expect(respuestas)
    @api.response(204, 'Respuestas successfully updated.')
    def put(self, encuesta_id): # para actuañizar, se usa el id_encuesta, pero realmente es el idde pregunta
        # aolo para actualizar
        """
        Updates a Respuestas
        """
        data = request.json        
        status = update_respuesta(encuesta_id, data) 
        if status == None:
            return "{'status':'Registro actualizado'}", 201
        else:
            return "{'status':'registro no actualizado'}", 404
            
            
@ns.route('/calificacion')
@api.response(404, 'Calificacion not found.')
class CalificacionItem(Resource):

    @api.marshal_with(respuestas)
    def get(self):
        """
        Returns calificaciones
        """
        return tbl_calificacion.query.all()


@ns.route('/respuestas/<int:encuesta_id>/<int:pregunta_id>')
@api.response(404, 'Respuesta filtrada por encuesta_id y pregunta_id')
class RespuestasItem(Resource):

    @api.marshal_with(respuestas)
    def get(self, encuesta_id, pregunta_id):
        """
        Return respuesta en funcion de la pregunta
        """
        respuestas = tbl_respuestas.query.filter(tbl_respuestas.encuesta_id == encuesta_id, tbl_respuestas.pregunta_id == pregunta_id).one()        
        if respuestas:            
            return respuestas
        else:
            respuestas = {
                    'status': '400',
                    'mensaje': 'No existen respuestas'
                }
            return respuestas, 404
