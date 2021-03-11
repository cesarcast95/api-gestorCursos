import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_cv, delete_cv, update_cv
from rest_api_si_empre.api.roles.serializers import cv, page_of_cv
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_cv
from sqlalchemy import exc


log = logging.getLogger(__name__)

ns = api.namespace('roles/cv', description='Operations related to cvs')


@ns.route('/')
class CvCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_cv)
    def get(self):
        """
        Returns list of cv.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        cv_query = Tbl_cv.query
        tbl_cv_page = cv_query.paginate(page, per_page, error_out=False)

        return tbl_cv_page

    @api.response(201, 'cv successfully created.')
    @api.expect(cv)
    def post(self):
        """
        Creates a new blog cv.
        """
        data = request.json
        create_cv(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Cv not found.')
class CvItem(Resource):

    @api.marshal_with(cv)
    def get(self, id):
        """
        Returns a group with a list of posts.
        """
        try:
            return Tbl_cv.query.filter(Tbl_cv.id_usuario == id).one()
        except exc.SQLAlchemyError:         
            return None, 404

    @api.expect(cv)
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
        update_cv(id, data)
        return None, 204

    @api.response(204, 'Group successfully deleted.')
    def delete(self, id):
        """
        Deletes blog group.
        """
        delete_cv(id)
        return None, 204
