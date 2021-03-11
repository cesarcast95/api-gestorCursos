import logging
from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.serializers import usuario, page_of_curso
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_usuario, Tbl_usuario_rol, tbl_roles, encrypt_string

import sqlalchemy


from sqlalchemy.orm import load_only

log = logging.getLogger(__name__)

ns = api.namespace('roles/login', description='Operaciones permitidas para login')


@ns.route('/')
class Login(Resource):
        
    def post(self):
        """
        Login a new rol.
        """
        response = {}
        roles_list = []
        data = request.json
        username = data['username']
        password = encrypt_string(data['password_hash'])        
        try:
            usuario = tbl_usuario.query.filter(tbl_usuario.username == username, tbl_usuario.password_hash == password, tbl_usuario.estado == 1).one()                                    
            id_usuario = usuario.id
            response['id_usuario'] = id_usuario
            response['nombres'] = usuario.nombre + ' ' + usuario.apellido                              
            roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_usuario == id_usuario).all()            
            for rol in roles:
                roles_dict = {}                
                aux = tbl_roles.query.filter(tbl_roles.id == rol.id_rol).options(load_only("descripcion")).one()                           
                roles_dict['nombre'] = aux.descripcion
                roles_list.append(roles_dict)
            response['roles'] = roles_list                        
            return response, 201
        except sqlalchemy.orm.exc.NoResultFound:
            return 'Credenciales incorrectas', 404