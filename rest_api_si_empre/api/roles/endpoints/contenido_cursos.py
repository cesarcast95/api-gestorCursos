import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_contenido, update_contenido, delete_contenido
from rest_api_si_empre.api.roles.serializers import contenido, page_of_contenido
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_contenido_curso

log = logging.getLogger(__name__)

ns = api.namespace('roles/cursos/contenido', description='Operaciones permitidas en contenido')


@ns.route('/')
class ContenidoCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_contenido)
    def get(self):
        """
        Returns list of contenido.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     

        contenido_query = tbl_contenido_curso.query
        contenido_page = contenido_query.paginate(page, per_page, error_out=False)

        return contenido_page

    
    @api.expect(contenido)
    def post(self):
        """
        Creates a new contenido.
        """
        create_contenido(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'contenido not found.')
class ContenidoItem(Resource):

    @api.marshal_with(contenido)
    def get(self, id):
        """
        Returns a contenido
        """
        return tbl_contenido_curso.query.filter(tbl_contenido_curso.id == id).one()

    @api.expect(contenido)
    @api.response(204, 'Contenido successfully updated.')
    def put(self, id):
        """
        Updates a contenido
        """
        data = request.json
        update_contenido(id, data)
        return None, 204

    @api.response(204, 'Contenido successfully deleted.')
    def delete(self, id):
        """
        Deletes contenido
        """
        delete_contenido(id)
        return None, 204

@ns.route('/curso/<int:id>')
@api.response(404, 'Curso not found.')
class CursoItem(Resource):

    @api.marshal_with(contenido)
    def get(self, id):
        """
        Returns a estudiantes
        """        
        return tbl_contenido_curso.query.filter(tbl_contenido_curso.id_curso == id).all()