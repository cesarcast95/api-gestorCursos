import logging
import os
from flask import request
from flask_restplus import Resource
from flask import jsonify

from rest_api_si_empre.api.roles.serializers import acta_docente, page_of_acta_docente,resource_fields
from rest_api_si_empre.api.roles.business import create_acta_docente, update_acta_docente, delete_acta_docente

from rest_api_si_empre.database.models import Tbl_acta_docente, tbl_curso_profesor

from rest_api_si_empre.api.roles.parsers import pagination_arguments
from rest_api_si_empre.api.restplus import api
#from rest_api_si_empre.database.models import 
from sqlalchemy import exc

from werkzeug.wrappers import Request
from werkzeug.utils import secure_filename
from flask import send_from_directory, send_file


log = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#UPLOAD_FOLDER_PROFESOR = os.path.join(BASE_DIR, '/media/acta_profesor')


ns = api.namespace('roles/acta_docente', description='Operaciones permitidas en acta_docente')



@ns.route('/')
class Acta_docenteCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_acta_docente)
    def get(self):
        """
        Returns list of acta_docente.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)     
        
        acta_docente_query = Tbl_acta_docente.query
        acta_docente_page = acta_docente_query.paginate(page, per_page, error_out=False)

        return acta_docente_page
    
    @api.expect(acta_docente)
    def post(self):
        """
        Creates a new acta_docente
        """
        data = request.json
        status = create_acta_docente(data)
        if status == 201:
            return "{'status':'Registro guardado'}", 201
        else:
            return "{'status':'No se puede ingresar más de 10 estudiantes por monitor'}", 403
            

@ns.route('/<int:id>')
@api.response(404, 'acta_docente not found.')
class Acta_docenteItem(Resource):

    @api.marshal_with(acta_docente)
    def get(self, id):
        """
        Returns a acta_docente
        """
        return Tbl_acta_docente.query.filter(Tbl_acta_docente.id == id).one()


    @api.expect(acta_docente)
    @api.response(204, 'Acta_docente succeefully updated.')
    def put(self, id):
        """
        Update a acta_docente
        """
        data = request.json
        status = update_acta_docente(id, data)
        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'No se puede actualizar'}", 403

    @api.expect(acta_docente)
    @api.response(204, 'User and rol successfully deleted.')
    def delete(self, id):
        """
        Deletes blog group.
        """
        delete_acta_docente(id)
        return None, 204



ALLOWED_EXTENSIONS = set(['docx'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@ns.route('/file-upload/<int:curso_profesor>/<int:seccion>')
@api.response(404, 'acta_docente not found.')
class Acta_docenteFile(Resource):

    def post(self,curso_profesor,seccion):
        # check if the post request has the file part                
        if 'file' not in request.files:
            print('no hay archivo')
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            print('no se sube el archivo')
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            name_storage = str(curso_profesor)+'-'+str(seccion)
            filename = name_storage+'.docx'
            file.save(os.path.join(BASE_DIR + '/media/acta-profesor', filename))
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message' : 'Allowed file types are docx'})
            resp.status_code = 400
            return resp


@ns.route('/docente/<int:id>')
@api.response(404, 'Monitoria not found.')
class ActasDocenteItem2(Resource):

    @api.marshal_with(acta_docente)
    def get(self, id):
        """
        Returns a monitoria
        """
        
        return Tbl_acta_docente.query.filter(Tbl_acta_docente.id_curso_profesor == id).all()


@ns.route('/docente_acta/<int:id>/<int:seccion>')
@api.response(404, 'Monitoria not found.')
class ActasDocenteItem2(Resource):

    @api.marshal_with(acta_docente)
    def get(self, id, seccion):
        """
        Returns a monitoria
        """
        
        return Tbl_acta_docente.query.filter(Tbl_acta_docente.id_curso_profesor == id,Tbl_acta_docente.seccion == seccion).all()


# @app.route('/media/posts/<filename>')
# def media_posts(filename):
#     dir_path = os.path.join(BASE_DIR + '/media/acta-profesor/')
#     return send_from_directory(dir_path, filename)

# @ns.route('/media/posts/<filename>')
# @api.response(404, 'Monitoria not found.')
# class Acta_docenteFile(Resource):
#     @api.marshal_with(acta_docente)
#     def get(self,filename):
#         f = open(BASE_DIR + '\\media\\acta-profesor\\' + filename, 'rb')
#         data={}
#         data['meet']=f
#         data['evidencia']=f.read()
#         return data
