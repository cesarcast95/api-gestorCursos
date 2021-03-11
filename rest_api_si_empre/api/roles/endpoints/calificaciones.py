import logging

from flask import request
from flask_restplus import Resource
#from rest_api_si_empre.api.roles.business import 
from rest_api_si_empre.api.roles.serializers import calificacion
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_calificacion
from sqlalchemy import exc

log = logging.getLogger(__name__)

ns = api.namespace('roles/calificaciones', description='Operaciones permitidas en calificaciones')

@ns.route('/')
class CalificacionesCollection(Resource):
    
    @api.marshal_with(calificacion)
    def get(self):
        """
        Lista de calificaciones
        """
        calificaciones = tbl_calificacion.query.all()        
        if calificaciones:            
            return calificaciones
        else: 
            calificacion_one = tbl_calificacion.query.first()
            if calificacion_one:
                return calificacion_one
            else:
                calificaciones = {}
                return None, 404