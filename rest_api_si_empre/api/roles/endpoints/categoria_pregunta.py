import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.serializers import categoria
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_categoria
from sqlalchemy import exc

log = logging.getLogger(__name__)

ns = api.namespace('roles/categoria', description='Operaciones permitidas en categoria')

@ns.route('/')
class CategoriaCollection(Resource):
    
    @api.marshal_with(categoria)
    def get(self):
        """
        Lista de categoria
        """
        categorias = tbl_categoria.query.all()        
        if categorias:            
            return categorias
        else: 
            categorias_one = tbl_categoria.query.first()
            if categorias_one:
                return categorias_one
            else:
                categorias = {}
                return None, 404