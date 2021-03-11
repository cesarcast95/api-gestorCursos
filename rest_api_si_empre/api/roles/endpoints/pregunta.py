import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_pregunta, update_pregunta
from rest_api_si_empre.api.roles.serializers import preguntas
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_preguntas
from sqlalchemy import exc

log = logging.getLogger(__name__)

ns = api.namespace('roles/pregunta', description='Operaciones permitidas en pregunta')

@ns.route('/')
class EncuestaCollection(Resource):
    
    @api.expect(preguntas)
    def post(self):
        """
        Creates a new pregunta
        """
        status = create_pregunta(request.json)
        if status != None:
            return "{'status':'No se pudo guardar el registro, consulte con el admin del sistema'}", 404            
        else:
            return "{'status':'Registro guardado'}", 201



@ns.route('/<int:id>')
@api.response(404, 'pregunta not found.')
class encuestas(Resource):

    @api.marshal_with(preguntas)
    def get(self, id):
        """
        Returns a encuesta
        """
        return tbl_preguntas.query.filter(tbl_preguntas.id == id).one()

    
    @api.expect(preguntas)
    @api.response(204, 'pregunta successfully updated.')
    def put(self, id):
        """
        Updates a pregunta
        """
        data = request.json
        status = update_pregunta(id, data)
        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'registro con incovenientes'}", 403



@ns.route('/all-preguntas')
@api.response(404, 'Preguntas not found.')
class PreguntaItem(Resource):

    @api.marshal_with(preguntas)
    def get(self):
        """
        Returns a preguntas
        """        
        return tbl_preguntas.query.order_by('id').all()