import logging
from flask import jsonify 

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_estudiante_grupo_curso, update_estudiante_grupo_curso, delete_estudiante_grupo_curso
from rest_api_si_empre.api.roles.serializers import estudiante_grupo_curso, page_of_estudiante_grupo_curso
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_estudiantes, Tbl_estudiante_grupo_curso, db


log = logging.getLogger(__name__)

ns = api.namespace('roles/estudiante_grupo_curso', description='Operaciones permitidas en estudiante_grupo_curso')


@ns.route('/')
class Estudiante_grupo_cursoCollection(Resource):


    
    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_estudiante_grupo_curso)
    def get(self):
        """
        Returns list of estudiante_grupo_curso.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)   

        estudiante_grupo_curso_query = Tbl_estudiante_grupo_curso.query
        tbl_estudiante_grupo_curso_page = estudiante_grupo_curso_query.paginate(page, per_page, error_out=False)

        return tbl_estudiante_grupo_curso_page

    
    @api.expect(estudiante_grupo_curso)
    def post(self):
        """
        Creates a new estudiante_grupo_curso.
        """
        status = create_estudiante_grupo_curso(request.json)        
        if status == 201:
            return "{'status':'Registro guardado'}", 201
        else:
            return "{'status':'No se puede ingresar más de 40 estudiantes por grupo'}", 403


@ns.route('/<int:id>')
@api.response(404, 'Estudiante_grupo_curso not found.')
class Estudiante_grupo_cursoItem(Resource):

    @api.marshal_with(estudiante_grupo_curso)
    def get(self, id):
        """
        Returns a estudiante_grupo_curso
        """
        return Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id == id).one()

    @api.expect(estudiante_grupo_curso)
    @api.response(204, 'Estudiante_grupo_curso successfully updated.')
    def put(self, id):
        """
        Updates a estudiante_grupo_curso
        """
        data = request.json
        status = update_estudiante_grupo_curso(id, data)

        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'No se puede ingresar más de 40 estudiantes por grupo'}", 403


    @api.response(204, 'Estudiante_grupo_curso successfully deleted.')
    def delete(self, id):
        """
        Deletes estudiante_grupo_curso.
        """
        delete_estudiante_grupo_curso(id)
        return None, 204




@ns.route('/detail/<int:id>')
@api.response(404, 'No se encontarron resultados')
class Estudiante_grupo_curso_lista(Resource):

    @api.marshal_list_with(estudiante_grupo_curso)
    def get(self, id):
        """
        Returns a estudiante_grupo_curso
        """        
        cursos = Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id_estudiante == id).all()        
        if cursos:            
            return cursos
        else:
            cursos = {}
            return None, 404

@ns.route('/cursos/<int:id_usuario>')
@api.response(404, 'No se encontarron resultados')
class Estudiante_grupo_curso_lista(Resource):

    @api.marshal_list_with(estudiante_grupo_curso)
    def get(self, id_usuario):
        """
        Returns a estudiante_grupo_curso
        """ 
        estudiante= Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == id_usuario).one()
        id_estudiante = estudiante.id 
        cursos = Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id_estudiante == id_estudiante).all()        
        if cursos:            
            return cursos
        else:
            cursos = {}
            return None, 404   
         


@ns.route('/curso/<int:id>')
@api.response(404, 'Curso not found.')
class CoordinadorItem(Resource):

    @api.marshal_with(estudiante_grupo_curso)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id_curso == id).all()


@ns.route('/grupo/<int:id>')
@api.response(404, 'Curso not found.')
class CoordinadorItem(Resource):

    @api.marshal_with(estudiante_grupo_curso)
    def get(self, id):
        """
        Returns a estudiantes
        """
        return Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id_grupo == id).all()



@ns.route('/estudiante-curso/<int:id_curso>')
@api.response(404, 'Curso not found.')
class EstudiantesCurso(Resource):

    @api.marshal_with(estudiante_grupo_curso)
    def get(self, id_curso):
        """
        Returns a estudiantes
        """
        return Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id_curso == id_curso).all()

@ns.route('/all-estudiantegrupocurso')
@api.response(404, 'Estudiantes, salones, cursos not found.')
class EstudianteSalonCurso(Resource):
    @api.marshal_with(estudiante_grupo_curso)
    def get(self):
        """
        Return estudiantes salones cursos
        """
        return Tbl_estudiante_grupo_curso.query.all()