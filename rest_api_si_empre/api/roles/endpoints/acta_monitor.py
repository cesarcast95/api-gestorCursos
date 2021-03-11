import logging
import os
from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_acta_monitor, update_acta_monitor, delete_acta_monitor
from rest_api_si_empre.api.roles.serializers import acta_monitor, page_of_acta_monitor
from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import Tbl_acta_monitor
from sqlalchemy import exc
from flask import jsonify
from werkzeug.utils import secure_filename

log = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# UPLOAD_FOLDER_PROFESOR = os.path.join(BASE_DIR, '../../media/acta_monitor/')



ns = api.namespace('roles/acta_monitor', description='Operaciones permitidas en acta_monitor')

@ns.route('/')
class Acta_monitorCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_acta_monitor)
    def get(self):
        """
        Returns list of acta_monitor.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     
        
        acta_monitor_query = Tbl_acta_monitor.query
        acta_monitor_page = acta_monitor_query.paginate(page, per_page, error_out=False)

        return acta_monitor_page
    
    @api.expect(acta_monitor)
    def post(self):
        """
        Creates a new acta monitor
        """
        status = create_acta_monitor(request.json)
        if status == 201:
            return "{'status':'Registro guardado'}", 201
        else:
            return "{'status':'No se puede ingresar más de 10 estudiantes por monitor'}", 403
            


@ns.route('/<int:id_acta_monitor>')
@api.response(404, 'Monitoria not found.')
class Acta_monitorItem(Resource):

    @api.marshal_with(acta_monitor)
    def get(self, id_acta_monitor):
        """
        Returns a acta monitor
        """
        return Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id == id_acta_monitor).one()

    @api.expect(acta_monitor)
    @api.response(204, 'Acta_monitor succeefully updated.')
    def put(self, id_acta_monitor):
        """
        Update a acta monitor
        """
        data = request.json
        status = update_acta_monitor(id_acta_monitor, data)
        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'No se puede ingresar más de 10 estudiantes por monitor'}", 403


# Hasta esta parte se tienen las funcionalidades necesarias para las actas ELIMINAR
    @api.response(204, 'User and rol successfully deleted.')
    def delete(self, id_acta_monitor):
        """
        Deletes blog group.
        """
        delete_acta_monitor(id_acta_monitor)
        return None, 204
# A continuación se da uso a la extensión para subir documentos x

ALLOWED_EXTENSIONS = set(['docx'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ns.route('/file-upload/<int:id_monitor>/<int:id_estudiante>')
@api.response(404, 'acta_docente not found.')
class Acta_monitorFile(Resource):

    def post(self, id_monitor, id_estudiante):
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            name_storage = str(id_monitor)+'-'+str(id_estudiante)
            filename = name_storage+'.docx'
            file.save(os.path.join(BASE_DIR + '/media/acta-monitor', filename))
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message' : 'Allowed file types are docx'})
            resp.status_code = 400
            return resp

@ns.route('/actasmonitor/<int:id_monitor>')
@api.response(404, "Acta monitor not found.")
class ActaPorMonitor(Resource):
    @api.marshal_with(acta_monitor)
    def get(self, id_monitor):
        from sqlalchemy import desc
        """
        Return actas por monitor 
        """
        return Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id_monitor == id_monitor).order_by(Tbl_acta_monitor.fecha.desc()).all()

@ns.route('/monitor/<int:id>')
@api.response(404, 'Monitoria not found.')
class Acta_monitorItem42(Resource):

    @api.marshal_with(acta_monitor)
    def get(self, id):
        """
        Returns a monitoria
        """
        return Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id_monitor == id).all()

@ns.route('/grupo/<int:id>')
@api.response(404, 'Monitoria not found.')
class Acta_monitorItem2(Resource):

    @api.marshal_with(acta_monitor)
    def get(self, id):
        """
        Returns a monitoria
        """
        return Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id_grupo == id).all()

@ns.route('/grupo/<int:id_grupo>/<int:id_monitor>')
@api.response(404, 'Monitoria not found.')
class Acta_monitorItem3(Resource):

    @api.marshal_with(acta_monitor)
    def get(self, id_grupo, id_monitor):
        """
        Returns a monitoria
        """
        return Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id_grupo == id_grupo, Tbl_acta_monitor.id_monitor == id_monitor).all()


@ns.route('/estudiantes/<int:id_monitor>')
@api.response(404, 'Monitoria not found.')
class Acta_monitorItem4(Resource):

    @api.marshal_with(acta_monitor)
    def get(self, id_monitor):
        """
        Returns a monitoria
        """
        return Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id_monitor == id_monitor).all()

