import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_mensajes, update_mensajes
from rest_api_si_empre.api.roles.serializers import mensajes, page_of_mensajes
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_mensaje, Tbl_estudiantes

import sqlalchemy

log = logging.getLogger(__name__)

ns = api.namespace(
    'roles/mensajes', description='Operaciones permitidas en mensajes')


@ns.route('/')
class MensajesCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_mensajes)
    def get(self):
        """
        Returns list of roles.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        mensajes_query = Tbl_mensaje.query
        tbl_mensajes_page = mensajes_query.paginate(
            page, per_page, error_out=False)

        return tbl_mensajes_page

    @api.expect(mensajes)
    def post(self):
        """
        Creates a new mensaje.
        """
        create_mensajes(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Mensaje not found.')
class MensajeItem(Resource):

    @api.marshal_with(mensajes)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return Tbl_mensaje.query.filter(Tbl_mensaje.id == id).one()

    @api.expect(mensajes)
    @api.response(204, 'Mensaje successfully updated.')
    def put(self, id):
        """
        Updates a Mensaje
        """
        data = request.json
        update_mensajes(id, data)
        return None, 204


@ns.route('/usuario/<int:id_usuario>')
@api.response(404, 'Mensaje not found.')
class MensajeUserItem(Resource):

    @api.marshal_with(mensajes)
    def get(self, id_usuario):
        """
        Returns a estudiantes
        """
        try:
            estudiante = Tbl_estudiantes.query.filter(
                Tbl_estudiantes.id_usuario == id_usuario).one()
            id_estu = estudiante.id
            mensajes = Tbl_mensaje.query.filter(
                    Tbl_mensaje.id_estudiante == id_estu).all()
            if mensajes:                         
                return mensajes                
            else:                
                mensajes = Tbl_mensaje.query.filter(
                    Tbl_mensaje.id_estudiante == id_estu).one()
                return mensajes

        except sqlalchemy.orm.exc.NoResultFound:
            return 'No hay Mensajes', 404