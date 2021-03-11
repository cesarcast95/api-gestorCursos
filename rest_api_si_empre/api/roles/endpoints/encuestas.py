import logging
import os
from flask import request
from flask_restplus import Resource
from rest_api_si_empre.api.roles.business import create_encuesta, update_encuesta
from rest_api_si_empre.api.roles.serializers import encuesta
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database.models import tbl_encuesta, tbl_respuestas, tbl_preguntas, tbl_estado
from sqlalchemy import exc
from flask import jsonify
from werkzeug.utils import secure_filename
import sqlalchemy
from rest_api_si_empre.database import db
from datetime import datetime



log = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ns = api.namespace('roles/encuesta', description='Operaciones permitidas en encuesta')

@ns.route('/')
class EncuestaCollection(Resource):
    
    @api.expect(encuesta)
    def post(self):
        """
        Creates a new encuesta
        """         
        status = create_encuesta(request.json)
        if status == None:
            return "{'status':'No se pudo guardar el registro, consulte con el admin del sistema'}", 404            
        else:
            return status, 201



@ns.route('/<int:id>')
@api.response(404, 'Encuestas not found.')
class encuestas(Resource):

    @api.marshal_with(encuesta)
    def get(self, id):
        """
        Returns a encuesta
        """
        return tbl_encuesta.query.filter(tbl_encuesta.id == id).one()

    @api.expect(encuesta)
    @api.response(204, 'encuesta successfully updated.')
    def put(self, id):
        """
        Updates a encuesta
        """
        data = request.json
        status = update_encuesta(id, data)       
        if status == 204:
            return "{'status':'Registro guardado'}", 204
        else:
            return "{'status':'registro con incovenientes'}", 403



@ns.route('/consultar/<int:id_asesoria>')
@api.response(404, 'Encuestas not found.')
class EncuestaForAsesoria(Resource):
    
    def get(self, id_asesoria):
        """
        Returns a encuesta
        Cuando encuentre una encuesta asociada a esa asesoria, retorna un 403,
        De lo contrario retorna un 200 que permite crear la nueva encuesta
        """
        try:
            encuesta = tbl_encuesta.query.filter(tbl_encuesta.asesorias_id == id_asesoria).one()
            dict_encuesta = {}       
            dict_encuesta['asesorias_id'] = encuesta.asesorias_id
            dict_encuesta['id'] = encuesta.id
            dict_encuesta['estado_id'] = encuesta.estado_id
            dict_encuesta['evidencia'] = encuesta.evidencia
            respuestas = tbl_respuestas.query.filter(tbl_respuestas.encuesta_id == encuesta.id).all()
            preguntas = tbl_preguntas.query.all()
            porcentaje = len(respuestas) * 100
            porcentaje = porcentaje // len(preguntas)
            dict_encuesta['num_respuestas'] = porcentaje
            return dict_encuesta, 403
        except sqlalchemy.orm.exc.NoResultFound:
            return {'status': '200',
                    'mensaje': 'Puede crear'}, 200




@ns.route('/cerrar-encuesta/<int:id_encuesta>')
@api.response(404, 'cerrar encuesta')
class EncuestaCerrar(Resource):
    
    def post(self, id_encuesta):
        data = request.json
        encuesta = tbl_encuesta.query.filter(tbl_encuesta.id == id_encuesta).one()
        encuesta.observacion = data['observacion']
        encuesta.evidencia = data['evidencia']
        estado = data['estado']
        print(estado, '#######')
        estado = tbl_estado.query.filter(tbl_estado.id == estado).one()
        encuesta.estado_id = estado.id
        encuesta.fecha_actualizacion = datetime.now()
        db.session.add(encuesta)
        db.session.commit()
        return 201

# A continuación se da uso a la extensión para subir documentos x

ALLOWED_EXTENSIONS = set(['docx'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ns.route('/file-upload/<int:encuesta_id>')
@api.response(404, 'Evidencia asesor not found.')
class Evidencia_AsesorFile(Resource):
    def post(self, encuesta_id):
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
            name_storage = str(encuesta_id)
            filename = name_storage+'.docx'
            file.save(os.path.join(BASE_DIR + '/media/evidencia-asesor', filename))
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message' : 'Allowed file types are jpg'})
            resp.status_code = 400
            return resp