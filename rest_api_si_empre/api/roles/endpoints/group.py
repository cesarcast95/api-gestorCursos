import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_group, delete_group, update_group
from rest_api_si_empre.api.roles.serializers import group, page_of_group
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_grupo

log = logging.getLogger(__name__)

ns = api.namespace('roles/group', description='Operations related to groups')


@ns.route('/')
class GroupCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_group)
    def get(self):
        """
        Returns list of blog categories.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        grupo_query = Tbl_grupo.query
        grupo_query_page = grupo_query.paginate(page, per_page, error_out=False)

        return  grupo_query_page

    @api.expect(group)
    def post(self):
        """
        Creates a new blog group.
        """

        create_group(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Group not found.')
class GroupItem(Resource):

    @api.marshal_with(group)
    def get(self, id):
        """
        Returns a group with a list of posts.
        """
        return Tbl_grupo.query.filter(Tbl_grupo.id == id).one()

    @api.expect(group)
    @api.response(204, 'Group successfully updated.')
    def put(self, id):
        """
        Updates a blog group.

        Use this method to change the name of a blog group.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Group Name"
        }
        ```

        * Specify the ID of the Group to modify in the request URL path.
        """
        data = request.json
        update_group(id, data)
        return None, 204

    @api.response(204, 'Group successfully deleted.')
    def delete(self, id):
        """
        Deletes blog group.
        """
        delete_group(id)
        return None, 204


@ns.route('/all')
@api.response(404, 'Group not found.')
class GroupItemAll(Resource):

    @api.marshal_with(group)
    def get(self):
        """
        Returns a group with a list of posts.
        """
        return Tbl_grupo.query.all()
