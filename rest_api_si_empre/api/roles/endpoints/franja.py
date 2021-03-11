import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_franja, update_franja, delete_franja
from rest_api_si_empre.api.roles.serializers import franja, page_of_franja
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_franja

log = logging.getLogger(__name__)

ns = api.namespace('roles/franja', description='Operaciones permitidas en franja')


@ns.route('/')
class FranjaCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_franja)
    def get(self):
        """
        Returns list of ranja.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        franja_query = Tbl_franja.query
        franja_page = franja_query.paginate(page, per_page, error_out=False)

        return franja_page

    
    @api.expect(franja)
    def post(self):
        """
        Creates a new franja.
        """
        create_franja(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Franja not found.')
class FranjaItem(Resource):

    @api.marshal_with(franja)
    def get(self, id):
        """
        Returns a franjass
        """
        return Tbl_franja.query.filter(Tbl_franja.id == id).one()

    @api.expect(franja)
    @api.response(204, 'Franja successfully updated.')
    def put(self, id):
        """
        Updates a franja
        """
        data = request.json
        update_franja(id, data)
        return None, 204

    @api.response(204, 'Franja successfully deleted.')
    def delete(self, id):
        """
        Deletes franja
        """
        delete_franja(id)
        return None, 204