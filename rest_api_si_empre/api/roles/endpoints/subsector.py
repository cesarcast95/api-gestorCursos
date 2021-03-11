import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_subsector, update_subsector
from rest_api_si_empre.api.roles.serializers import subsector, page_of_subsector
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_subsector

log = logging.getLogger(__name__)

ns = api.namespace('roles/subsector', description='Operaciones permitidas en subsector')


@ns.route('/')
class SubsectorCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_subsector)
    def get(self):
        """
        Returns list of subsector.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page',50)     

        subsector_query = tbl_subsector.query
        subsector_page = subsector_query.paginate(page, per_page, error_out=False)

        return subsector_page
    
    @api.expect(subsector)
    def post(self):
        """
        Creates a new subsector.
        """
        create_subsector(request.json)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Subsector not found.')
class SubsectorItem(Resource):
    @api.marshal_with(subsector) 
    def get(self, id):
        """
        Return subsectores
        """
        return tbl_subsector.query.filter(tbl_subsector.id == id).one()
    @api.expect(subsector)
    @api.response(204, 'Subsector successfully updated.')
    def put(self, id):
        """
        updates a subsector
        """
        data = request.json
        update_subsector(id, data)
        return None, 204

@ns.route('/all-subsector')
@api.response(404, 'Usuarios not found.')
class SubsectorAll(Resource):

    @api.marshal_with(subsector)
    def get(self):
        """
        Returns a usuarios
        """
        return tbl_subsector.query.all()