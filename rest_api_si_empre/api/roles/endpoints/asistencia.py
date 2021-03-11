import logging
from flask import jsonify 

from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_asistencia, update_asistencia, delete_asistencia
from rest_api_si_empre.api.roles.serializers import asistencia, page_of_asistencia
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_asistencia, db


log = logging.getLogger(__name__)

ns = api.namespace('roles/asistencia', description='Operaciones permitidas en asistencia')


@ns.route('/')
class AsistenciaCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_asistencia)
    def get(self):
        """
        Returns list of asistencia.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)   

        asistencia_query = Tbl_asistencia.query
        tbl_asistencia_page = asistencia_query.paginate(page, per_page, error_out=False)

        return tbl_asistencia_page

    
    @api.expect(asistencia)
    def post(self):
        """
        Creates a new asistencia.
        """
        status = create_asistencia(request.json)

        if status == 201:
            return "{'status':'Registro guardado'}", 201
        else:
            return "{'status':'No se puede ingresar más de 40 estudiantes por grupo'}", 403


@ns.route('/<int:id>')
@api.response(404, 'asistencia not found.')
class AsistenciaItem(Resource):

    @api.marshal_with(asistencia)
    def get(self, id):
        """
        Returns a asistencia
        """
        return Tbl_asistencia.query.filter(Tbl_asistencia.id == id).one()

    @api.expect(asistencia)
    @api.response(204, 'asistencia successfully updated.')
    def put(self, id):
        """
        Updates a asistencia
        """
        data = request.json
        status = update_asistencia(id, data)

        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'No se puede ingresar más de 40 estudiantes por grupo'}", 403


    @api.response(204, 'asistencia successfully deleted.')
    def delete(self, id):
        """
        Deletes asistencia.
        """
        delete_asistencia(id)
        return None, 204


@ns.route('curso-profesor/<int:id_curso>')
@api.response(404, 'asistencia not found.')
class AsistenciaCursoProfesor(Resource):

    @api.marshal_with(asistencia)
    def get(self, id_curso):
        """
        Returns a asistencia
        """        
        return Tbl_asistencia.query.filter(Tbl_asistencia.id_curso == id_curso).all()


@ns.route('curso-profesor/<int:id_curso>/session/<int:session>')
@api.response(404, 'asistencia not found.')
class AsistenciaCursoProfesorSession(Resource):

    @api.marshal_with(asistencia)
    def get(self, id_curso, session):
        """
        Returns a asistencia
        """                
        return Tbl_asistencia.query.filter(Tbl_asistencia.id_curso == id_curso, Tbl_asistencia.seccion == session).all()

@ns.route('/asistencia_docente/<int:id>/<int:seccion>')
@api.response(404, 'Monitoria not found.')
class AsistenciaDocenteItem2(Resource):

    @api.marshal_with(asistencia)
    def get(self, id, seccion):
        """
        Returns a monitoria
        """
        
        return Tbl_asistencia.query.filter(Tbl_asistencia.id_curso == id,Tbl_asistencia.seccion == seccion).all()
