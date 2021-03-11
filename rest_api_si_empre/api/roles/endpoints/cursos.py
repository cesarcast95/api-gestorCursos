import logging
from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_roles_curso, delete_curso, update_curso
from rest_api_si_empre.api.roles.serializers import curso, page_of_curso
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_curso
from rest_api_si_empre.api.roles.endpoints.login import Login

log = logging.getLogger(__name__)

ns = api.namespace('roles/curso', description='Operaciones permitidas en cursos')


@ns.route('/')
class RolesCollection(Resource):
    
    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_curso)
    def get(self):
        """
        Returns list of roles.
        """   
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     
        curso_query = tbl_curso.query
        tbl_curso_page = curso_query.paginate(page, per_page, error_out=False)
                
        return tbl_curso_page

    
    @api.expect(curso)
    def post(self):
        """
        Creates a new rol.
        """
        create_roles_curso(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Curso not found.')
class CursoItem(Resource):

    @api.marshal_with(curso)
    def get(self, id):
        """
        Returns a estudiantes
        """        
        return tbl_curso.query.filter(tbl_curso.id == id).one()

    @api.expect(curso)
    @api.response(204, 'Curso successfully updated.')
    def put(self, id):
        """
        Updates a Estudiante
        """
        data = request.json
        update_curso(id, data)
        return None, 204

    @api.response(204, 'Curso successfully deleted.')
    def delete(self, id):
        """
        Deletes curso.
        """
        delete_curso(id)
        return None, 204


@ns.route('/profesor/<int:id>')
@api.response(404, 'Curso not found.')
class ProfesorItem(Resource):

    @api.marshal_with(curso)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return tbl_curso.query.filter(tbl_curso.id_profesor == id).all()


@ns.route('/coordinador/<int:id>')
@api.response(404, 'Curso not found.')
class CoordinadorItem(Resource):

    @api.marshal_with(curso)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return tbl_curso.query.filter(tbl_curso.id_coordinador == id).all()

@ns.route('/all-cursos')
@api.response(404, 'Cursos not found.')
class CursoItemAll(Resource):

    @api.marshal_with(curso)
    def get(self):
        """
        Returns a all list of cursos.
        """
        return tbl_curso.query.all()