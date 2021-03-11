import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_roles_roles, update_roles, delete_roles
from rest_api_si_empre.api.roles.serializers import roles_roles, page_of_roles_roles
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_roles

log = logging.getLogger(__name__)

ns = api.namespace('roles/rol', description='Operaciones permitidas en roles')


@ns.route('/')
class RolesCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_roles_roles)
    def get(self):
        """
        Returns list of roles.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        roles_query = tbl_roles.query
        roles_page = roles_query.paginate(page, per_page, error_out=False)

        return roles_page

    
    @api.expect(roles_roles)
    def post(self):
        """
        Creates a new rol.
        """
        create_roles_roles(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Roles not found.')
class RolesItem(Resource):

    @api.marshal_with(roles_roles)
    def get(self, id):
        """
        Returns a roles
        """
        return tbl_roles.query.filter(tbl_roles.id == id).one()

    @api.expect(roles_roles)
    @api.response(204, 'Roles successfully updated.')
    def put(self, id):
        """
        Updates a roles
        """
        data = request.json
        update_roles(id, data)
        return None, 204

    @api.response(204, 'Post successfully deleted.')
    def delete(self, id):
        """
        Deletes blog post.
        """
        delete_roles(id)
        return None, 204