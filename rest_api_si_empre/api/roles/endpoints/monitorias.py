import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_monitorias, update_monitorias, delete_acta_monitor
from rest_api_si_empre.api.roles.serializers import monitorias, page_of_monitorias
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_monitorias
from sqlalchemy import exc

log = logging.getLogger(__name__)

ns = api.namespace('roles/monitorias', description='Operaciones permitidas en monitorias')

@ns.route('/')
class MonitoriasCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_monitorias)
    def get(self):
        """
        Returns list of monitorias.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     
        
        monitorias_query = Tbl_monitorias.query
        monitorias_page = monitorias_query.paginate(page, per_page, error_out=False)

        return monitorias_page
    
    @api.expect(monitorias)
    def post(self):
        """
        Creates a new monitoria
        """
        status = create_monitorias(request.json)
        if status == 201:
            return "{'status':'Registro guardado'}", 201
        else:
            return "{'status':'No se puede ingresar más de 10 estudiantes por monitor'}", 403
            

@ns.route('/<int:id>')
@api.response(404, 'Monitoria not found.')
class MonitoriasItem(Resource):

    @api.marshal_with(monitorias)
    def get(self, id):
        """
        Returns a monitoria
        """
        return Tbl_monitorias.query.filter(Tbl_monitorias.id == id).one()

    @api.expect(monitorias)
    @api.response(204, 'Monitorias succeefully updated.')
    def put(self, id):
        """
        Update a monitoria
        """
        data = request.json
        status = update_monitorias(id, data)


        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'No se puede ingresar más de 10 estudiantes por monitor'}", 403


        
@ns.route('/monitor/<int:id>')
@api.response(404, 'Monitoria not found.')
class MonitoriasItem45(Resource):

    @api.marshal_with(monitorias)
    def get(self, id):
        """
        Returns a monitoria
        """
        return Tbl_monitorias.query.filter(Tbl_monitorias.id_monitor == id).first()

@ns.route('/grupo/<int:id>')
@api.response(404, 'Monitoria not found.')
class MonitoriasItem2(Resource):

    @api.marshal_with(monitorias)
    def get(self, id):
        """
        Returns a monitoria
        """
        return Tbl_monitorias.query.filter(Tbl_monitorias.id_grupo == id).all()

@ns.route('/grupo/<int:id_grupo>/<int:id_monitor>')
@api.response(404, 'Monitoria not found.')
class MonitoriasItem3(Resource):

    @api.marshal_with(monitorias)
    def get(self, id_grupo, id_monitor):
        """
        Returns a monitoria
        """
        return Tbl_monitorias.query.filter(Tbl_monitorias.id_grupo == id_grupo, Tbl_monitorias.id_monitor == id_monitor).all()


@ns.route('/estudiantes/<int:id_monitor>')
@api.response(404, 'Monitoria not found.')
class MonitoriasItem4(Resource):

    @api.marshal_with(monitorias)
    def get(self, id_monitor):
        """
        Returns a monitoria
        """
        return Tbl_monitorias.query.filter(Tbl_monitorias.id_monitor == id_monitor).all()

@ns.route('/all-monitorias')
@api.response(404, 'Monitorias not found')
class AllMonitoriasItem(Resource):
    @api.marshal_with(monitorias)
    def get(self):
        """
        Return all monitorias
        """
        return Tbl_monitorias.query.all()