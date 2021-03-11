import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_usuario, update_usuario, delete_usuario
from rest_api_si_empre.api.roles.serializers import usuario, page_of_usuario
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_usuario
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

log = logging.getLogger(__name__)

ns = api.namespace('roles/usuario', description='Operaciones permitidas en usuarios')


@ns.route('/')
class UsuariosCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_usuario)
    def get(self):
        """
        Returns list of usuarios.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        usuario_query = tbl_usuario.query
        tbl_usuario_page = usuario_query.paginate(page, per_page, error_out=False)

        return tbl_usuario_page

    
    @api.expect(usuario)
    def post(self):
        """
        Creates a new usuario.
        """
        r = create_usuario(request.json)        
        return r, 201


@ns.route('/<int:id>')
@api.response(404, 'Usuarios not found.')
class RolesItem(Resource):

    @api.marshal_with(usuario)
    def get(self, id):
        """
        Returns a usuarios
        """
        return tbl_usuario.query.filter(tbl_usuario.id == id).one()

    @api.expect(usuario)
    @api.response(204, 'Usuario successfully updated.')
    def put(self, id):
        """
        Updates a Usuario
        """
        data = request.json
        update_usuario(id, data)
        return None, 204

    @api.response(204, 'Usuario successfully deleted.')
    def delete(self, id):
        """
        Deletes usuario.
        """
        delete_usuario(id)
        return None, 204

@ns.route('/login')
class Login(Resource):
    """
    User Login Resource
    """
    @api.doc('user login')
    @api.expect(current_user, validate=True)
    def post(self):
        post_data = request.json


@ns.route('/all-usuarios')
@api.response(404, 'Usuarios not found.')
class RolesItem(Resource):

    @api.marshal_with(usuario)
    def get(self):
        """
        Returns a usuarios
        """
        return tbl_usuario.query.filter(tbl_usuario.delete==False).all() 



        

