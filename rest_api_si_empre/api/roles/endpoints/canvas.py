import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_canvas, update_canvas, delete_canvas
from rest_api_si_empre.api.roles.serializers import canvas, page_of_canvas
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_canvas

log = logging.getLogger(__name__)

ns = api.namespace('roles/canvas', description='Operaciones permitidas en canvas')


@ns.route('/')
class canvasCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_canvas)
    def get(self):
        """
        Returns list of canvas.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        canvas_query = tbl_canvas.query
        canvas_page = canvas_query.paginate(page, per_page, error_out=False)

        return canvas_page

    
    @api.expect(canvas)
    def post(self):
        """
        Creates a new canvas.
        """
        create_canvas(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'canvas not found.')
class canvasItem(Resource):

    @api.marshal_with(canvas)
    def get(self, id):
        """
        Returns a canvas
        """
        return tbl_canvas.query.filter(tbl_canvas.id == id).one()

    @api.expect(canvas)
    @api.response(204, 'canvas successfully updated.')
    def put(self, id):
        """
        Updates a canvas
        """
        data = request.json
        update_canvas(id, data)
        return None, 204

    @api.response(204, 'canvas successfully deleted.')
    def delete(self, id):
        """
        Deletes canvas
        """
        delete_canvas(id)
        return None, 204


@ns.route('/usuario/<int:id_usuario>')
@api.response(404, 'canvas not found.')
class canvasItem(Resource):

    @api.marshal_with(canvas)
    def get(self, id_usuario):
        """
        Returns a canvas
        """
        return tbl_canvas.query.filter(tbl_canvas.id_usuario == id_usuario).all()

