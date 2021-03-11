import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_usuario_rol, delete_usuario_rol, update_usuario_rol
from rest_api_si_empre.api.roles.serializers import usuario_rol, page_of_usuario_rol
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_usuario_rol
log = logging.getLogger(__name__)

ns = api.namespace('roles/usuario_rol', description='Operations related to users and rols')


@ns.route('/')
class UsuarioRolCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_usuario_rol)
    def get(self):
        """
        Returns list of usuario and rols.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        usuario_rol_query = Tbl_usuario_rol.query
        tbl_usuario_rol_page = usuario_rol_query.paginate(page, per_page, error_out=False)

        return tbl_usuario_rol_page

    @api.response(201, 'users and rols successfully created.')
    @api.expect(usuario_rol)
    def post(self):
        """
        Creates a new blog users and rols.
        """
        data = request.json
        create_usuario_rol(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Users and rols not found.')
class UsuarioRolItem(Resource):

    @api.marshal_with(usuario_rol)
    def get(self, id):
        """
        Returns a group with a list of posts.
        """
        return Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id == id).one()

    @api.expect(usuario_rol)
    @api.response(204, 'Users and rols successfully updated.')
    def put(self, id):
        """
        Updates a usuario rol.

        """
        data = request.json
        status = update_usuario_rol(id, data)

        if status == 204:
            return "{'status': 'Registro guardado'}", 204
        else:
            return "{'status': 'Error'}", 403

    @api.response(204, 'User and rol successfully deleted.')
    def delete(self, id):
        """
        Deletes blog group.
        """
        delete_usuario_rol(id)
        return None, 204




@ns.route('/usuario/<int:id_usuario>')
@api.response(404, 'Users and rols not found.')
class UsuarioRolesItem(Resource):

    @api.marshal_with(usuario_rol)
    def get(self, id_usuario):
        """
        Returns a group with a list of posts.
        """        
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_usuario == id_usuario).all()        
        if roles:            
            return roles
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_usuario == id_usuario).one()
        return roles



@ns.route('/monitores')
@api.response(404, 'Users and rols not found.')
class UsuarioRolesItem(Resource):

    @api.marshal_with(usuario_rol)
    def get(self):
        """
        Returns all monitores.
        """        
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 4).all()        
        if roles:            
            return roles
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 4).one()
        return roles



@ns.route('/profesores')
@api.response(404, 'Users and rols not found.')
class UsuarioRolesItem(Resource):

    @api.marshal_with(usuario_rol)
    def get(self):
        """
        Returns a group with a list of posts.
        """        
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 3).all()        
        if roles:            
            return roles
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 3).one()
        return roles

@ns.route('/estudiantes')
@api.response(404, 'Users and rols not found')
class UsuarioRolesItem(Resource):

    @api.marshal_with(usuario_rol)
    def get(self):
        """
        Returns a group with a list of posts.
        """
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 5).all()        
        if roles:            
            return roles
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 5).one()
        return roles

@ns.route('/asesores')
@api.response(404, 'Users and rols not found.')
class UsuarioRolesItem(Resource):

    @api.marshal_with(usuario_rol)
    def get(self):
        """
        Returns a group with a list of posts.
        """        
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 6).all()        
        if roles:            
            return roles
        roles = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id_rol == 6).one()
        return roles

@ns.route('/all-usuariorol')
@api.response(404, 'UsuarioRoll not found.')
class UsuarioRolesItems(Resource):
    @api.marshal_with(usuario_rol)
    def get(self):
        """
        Return all users and roles
        """
        return Tbl_usuario_rol.query.all()