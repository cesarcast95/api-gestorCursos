import logging

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_curso_profesor, update_curso_profesor, delete_curso_profesor
from rest_api_si_empre.api.roles.serializers import curso_profesor, page_of_curso_profesor
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_curso_profesor
log = logging.getLogger(__name__)

ns = api.namespace('roles/curso_profesor', description='Operations related to courses teachers')


@ns.route('/')
class CursoProfesorRolCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_curso_profesor)
    def get(self):
        """
        Returns list of usuario and rols.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)   

        curso_profesor_query = tbl_curso_profesor.query
        tbl_curso_profesor_page = curso_profesor_query.paginate(page, per_page, error_out=False)

        return tbl_curso_profesor_page

    @api.response(201, 'users and rols successfully created.')
    @api.expect(curso_profesor)
    def post(self):
        """
        Creates a new blog users and rols.
        """
        data = request.json
        create_curso_profesor(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Users and rols not found.')
class CursoProfesorItem(Resource):

    @api.marshal_with(curso_profesor)
    def get(self, id):
        """
        Returns a group with a list of posts.
        """
        return tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id).one()

    @api.expect(curso_profesor)
    @api.response(204, 'Users and rols successfully updated.')
    def put(self, id):
        """
        Updates a usuario rol.

        """
        data = request.json
        status = update_curso_profesor(id, data)

        if status == 204:
            return "{'status': 'Registro guardado'}", 204
        else:
            return "{'status': 'Error'}", 403

    @api.response(204, 'User and rol successfully deleted.')
    def delete(self, id):
        """
        Deletes blog group.
        """
        delete_curso_profesor(id)
        return None, 204
    
@ns.route('/profesor/<int:id_curso>')
@api.response(404, 'Users and rols not found.')
class ProfesorCursoItem(Resource):

    @api.marshal_with(curso_profesor)
    def get(self, id_curso):
        """
        Returns a group with a list of posts.
        """  

        roles = tbl_curso_profesor.query.filter(tbl_curso_profesor.id_curso == id_curso).all()        
        if roles:            
            return roles
        else: 
            roles2 = tbl_curso_profesor.query.filter(tbl_curso_profesor.id_curso == id_curso).first()
            if roles2:
                return roles2
            else:
                roles = {}
                return None, 404

@ns.route('/cursos/<int:id_docente>')
@api.response(404, 'Users and rols not found.')
class CursosItem(Resource):

    @api.marshal_with(curso_profesor)
    def get(self, id_docente):
        """
        Returns a group with a list of posts.
        """  

        cursos = tbl_curso_profesor.query.filter(tbl_curso_profesor.id_profesor == id_docente).all()        
        if cursos:            
            return cursos
        else:
            cursos = {}
            return None, 404


@ns.route('/cursos_profesor')
@api.response(404, 'Users and rols not found.')
class CursosProfesorItem(Resource):

    @api.marshal_with(curso_profesor)
    def get(self):
        """
        Returns a group with a list of posts.
        """  
        cursos = tbl_curso_profesor.query.filter().all()        
        if cursos:            
            return cursos
        else:
            cursos = {}
            return None, 404