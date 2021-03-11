from flask_restplus import fields
from rest_api_si_empre.api.restplus import api
from rest_api_si_empre.database import db


roles_roles = api.model('roles tbl_roles', {
    'id': fields.Integer(readOnly=True, description='Identificador unico para roles'),
    'descripcion': fields.String(required=True, description='Descripcion del rol')
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_roles_roles = api.inherit('Page of roles', pagination, {
    'items': fields.List(fields.Nested(roles_roles))
})

group = api.model('grupo', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the group'),
    'descripcion': fields.String(required=True, description='Description of group'),
})

page_of_group = api.inherit('Page of grupo', pagination, {
    'items':  fields.List(fields.Nested(group))
})

franja = api.model('Franja', {
    'id': fields.Integer(readOnly=True, description='Clave para identificar la franja'),
    'nombre': fields.String(required=True, description='Nombre franja'),
})

page_of_franja = api.inherit('Page of franja', pagination, {
    'items': fields.List(fields.Nested(franja))
})

contenido = api.model('Contenido', {
    'id': fields.Integer(readOnly=True, description='Clave para identificar el contenido'),
    'contenido': fields.String(required=True, description='Nombre Contenido'),
    'id_curso': fields.Integer(attribute='curso.id',description='identificador curso'),
    'titulo_curso': fields.String(attribute='curso.curso.titulo')

})

page_of_contenido = api.inherit('Page of contenido', pagination, {
    'items': fields.List(fields.Nested(contenido))
})

estudiante = api.model('Estudiante', {
    'id': fields.Integer(readOnly=True, description='Clave para identificar el estudiante'),
    'id_usuario': fields.Integer(attribute='usuario.id',description='Usuario'),
    'nombre_usuario': fields.String(attribute='usuario.nombre', description='Nombre estudiante'),
    'apellido_usuario': fields.String(attribute='usuario.apellido', description='Apellido estudiante'),
    'identificacion': fields.String(attribute='usuario.identificacion', description='Identificación estudiante'),
    'password': fields.String(attribute='usuario.password', description='Password estudiante'),
    'latitud': fields.Float(),
    'longitud': fields.Float(),
    'activo': fields.Boolean(default=False, description='El estudiante está activo'),
    'empresa': fields.String(escription='empresa'),
    'barrio_p': fields.String(description='barrio_p'),
    'comuna_p': fields.String(description='comuna_p'),
    'corregimiento_p': fields.String(description='corregimiento_p'),
    'id_subsector': fields.Integer(attribute='subsector.id',escription='Estudiante Subsector id'),
    'actividad_e': fields.String(description='actividad_e'),
    'direccion_e': fields.String(description='direccion_e'),
    'barrio_e': fields.String(description='barrio_e'),
    'comuna_e': fields.String(description='comuna_e'),
    'corregimiento_e': fields.String(description='corregimiento_e'),
    'num_whatsapp': fields.String(description='num_whatsapp'),
    'facebook': fields.String(description='facebook'),
    'instagram': fields.String(description='instagram'),
    'pagina_web': fields.String(description='pagina_web'),
    'otra_red_social': fields.String(description='otra_red_social'),
    'num_movil_e': fields.String(description='num_movil_e'),
    'num_emp': fields.Integer(description='num_emp'),
    'ano_fun': fields.Integer(description='ano_fun'),
    'per_emp': fields.String(description='per_emp'),
    'certificado': fields.String(description='certificado'),
   
})


page_of_estudiante = api.inherit('Page of estudiante', pagination, {
    'items': fields.List(fields.Nested(estudiante))
})


usuario = api.model('Usuario', {
    'id': fields.Integer(readOnly=True, description='Clave para identificar el Usuario'),
    'nombre': fields.String(required=True, description='Nombre Usuario'),
    'apellido': fields.String(required=True, description='Apellido Usuario'),
    'username': fields.String(required=True, description='Username Usuario'),
    'password_hash': fields.String(required=True, description='Password Usuario'),
    'identificacion': fields.String(required=True, description='Identificación Usuario'),
    'email': fields.String(required=True, description='Email Usuario'),
    'direccion': fields.String(required=True, description='Direccion Usuario'),
    'telefono': fields.String(required=True, description='Telefono Usuario'),
    'estado': fields.Boolean(required=True, description='Estado Usuario'),
    'delete': fields.Boolean(required=True, description='Delete Usuario'),
})

page_of_usuario = api.inherit('Page of Usuario', pagination, {
    'items': fields.List(fields.Nested(usuario))
})

class AuthDto:
    usuario_auth = api.model('auth_details', {
        'email': fields.String(required=True, description="Correo electronico"),
        'password': fields.String(required=True, description="Password"),
    })

curso = api.model('roles tbl_curso', {
    'id': fields.Integer(readOnly=True, description='Identiicador unico'),
    'titulo': fields.String(required=True, description="Nombre del curso"),
    'descripcion': fields.String(required=True, description="Descripcion del curso"),
    'objetivo': fields.String(required=True, description="Objetivo del curso"),
    'url': fields.String(required=True, description="Url del material"),
    'id_coordinador': fields.Integer(attribute='coordinador.id',escription='Usuario Coordinador'),
    'coordinador_profesor': fields.String(attribute='coordinador.nombre'),
    'coordinador_profesor_apellido': fields.String(attribute='coordinador.apellido'),
})

page_of_curso = api.inherit('Page of curso', pagination, {
    'items': fields.List(fields.Nested(curso))
})


cv = api.model('cv', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the cv'),
    'grado_academico': fields.String(required=True, description='field od academy grade'),
    'postgrado': fields.String(required=True, description='field of postgrado'),
    'profesion': fields.String(required=True, description='field of profession'),
    'id_usuario': fields.Integer(attribute='usuario.id'),
    'usuario': fields.String(attribute='usuario.nombre'),
    'cv_lac': fields.String(required=True, description='cv_lac'),
    'perfil': fields.String(required=True, description='perfil'),
    'experiencia': fields.String(required=True, description='experiencia'),
    'area_con': fields.String(required=True, description='area_con'),
    'curso_dicta': fields.String(required=True, description='curso_dicta'),

})

page_of_cv = api.inherit('Page of cv', pagination, {
    'items': fields.List(fields.Nested(cv))
})


estudiante_grupo_curso = api.model('Estudiante_grupo_curso', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the estudiante_grupo_curso'),
    'id_estudiante' : fields.Integer(attribute='estudiante.id'),
    'estudiante' : fields.String(attribute='estudiante.id_usuario'),
    'apellido_estudiante': fields.String(attribute='estudiante.usuario.apellido'),
    'nombre_estudiante': fields.String(attribute='estudiante.usuario.nombre'),
    'telefono_estudiante': fields.String(attribute='estudiante.usuario.telefono'),
    'email_estudiante': fields.String(attribute='estudiante.usuario.email'),
    'empresa_estudiante': fields.String(attribute='estudiante.empresa'),
    'id_grupo': fields.Integer(attribute='grupo.id'),
    'grupo': fields.String(attribute='grupo.descripcion'),
    'id_curso': fields.Integer(attribute='curso.id'),    
    'titulo': fields.String(attribute='curso.curso.titulo'),
    'url': fields.String(attribute='curso.curso.url'),
    'coordinador_profesor': fields.String(attribute='curso.curso.coordinador.nombre'),
    'id_profesor': fields.String(attribute='curso.id_profesor'),
    'id_cur': fields.String(attribute='curso.id'),
    
})

page_of_estudiante_grupo_curso = api.inherit('Page of estudiante_grupo_curso', pagination, {
    'items': fields.List(fields.Nested(estudiante_grupo_curso))
})

subsector = api.model('Subsector', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the subsector'),
    'nombre' : fields.String(required=True, description='subsector'),
})

page_of_subsector = api.inherit('Page of subsector', pagination, {
    'items': fields.List(fields.Nested(subsector))
})


programacion = api.model('roles programacion', {
    'id': fields.Integer(readOnly=True, description='Identiicadorunico'),
    'id_curso': fields.Integer(attribute='curso.id'),
    'id_franja': fields.Integer(attribute='franja.id'),
    'titulo_curso': fields.String(attribute='curso.curso.titulo'),
    'grupo': fields.String(attribute='curso.grupo.descripcion'),
    'nombre_franja': fields.String(attribute='franja.nombre'),
    'seccion': fields.Integer(description='Numero de seccion'),
    'meet' : fields.String(required=True, description="Meet"),
    'fecha' : fields.String(required=True, description="Fecha"),
})

page_of_programacion = api.inherit('Page of programacion', pagination, {
    'items': fields.List(fields.Nested(programacion))
})
usuario_rol = api.model('usuario_rol', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the user and rol'),
    'id_usuario': fields.Integer(attribute='usuario.id'),
    'id_rol': fields.Integer(attribute='rol.id'),
    'nombre_usuario': fields.String(attribute='usuario.nombre'),
    'apellido_usuario': fields.String(attribute='usuario.apellido'),
    'descripcion_rol': fields.String(attribute='rol.descripcion'),

})

page_of_usuario_rol = api.inherit('Page of usuario_rol', pagination, {
    'items': fields.List(fields.Nested(usuario_rol))
})

monitorias = api.model('monitorias', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the monitorias'),
    'id_monitor': fields.Integer(attribute='monitor.id'),
    'nombre_monitor': fields.String(attribute='monitor.nombre'),
    'apellido_monitor': fields.String(attribute='monitor.apellido'),
    'email_monitor': fields.String(attribute='monitor.email'),
    'telefono_monitor': fields.String(attribute='monitor.telefono'),
    'id_estudiante': fields.Integer(attribute='estudiante.id'),
    'id_usuario': fields.Integer(attribute='estudiante.usuario.id'),
    'nombre_estudiante': fields.String(attribute='estudiante.usuario.nombre'),
    'apellido_estudiante': fields.String(attribute='estudiante.usuario.apellido'),
    'telefono_estudiante': fields.String(attribute='estudiante.usuario.telefono'),
    'email_estudiante': fields.String(attribute='estudiante.usuario.email'),
    'id_grupo': fields.Integer(attribute='grupo.id'),
    'nombre_grupo': fields.String(attribute='grupo.descripcion'),
})

page_of_monitorias = api.inherit('Page of monitorias', pagination, {
    'items': fields.List(fields.Nested(monitorias))
})


mensajes = api.model('mensajes', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the mensajes'),
    'id_usuario': fields.Integer(attribute='usuario.id'),
    'nombre_usuario': fields.String(attribute='usuario.nombre'),
    'id_estudiante': fields.Integer(attribute='estudiante.usuario.id'),
    'nombre_estudiante': fields.String(attribute='estudiante.usuario.nombre'),
    'mensaje': fields.String(required=True, description="Comentario"),
    'created': fields.String(readOnly=True)
})


page_of_mensajes = api.inherit('Page of mensajes', pagination, {
    'items': fields.List(fields.Nested(mensajes))
})

asistencia = api.model('asistencia', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the estudiante_grupo_curso'),
    'id_estudiante' : fields.Integer(attribute='estudiante.id'),
    'nombre_estudiante' : fields.String(attribute='estudiante.usuario.nombre'),
    'apellido_estudiante' : fields.String(attribute='estudiante.usuario.apellido'),
    'id_curso': fields.Integer(attribute='curso.curso.id'),
    'nombre_estudiante': fields.String(attribute='estudiante.usuario.nombre'),
    'apellido_estudiante': fields.String(attribute='estudiante.usuario.apellido'),
    'telefono_estudiante': fields.String(attribute='estudiante.usuario.telefono'),
    'empresa_estudiante': fields.String(attribute='estudiante.empresa'),
    'titulo_curso': fields.String(attribute='curso.curso.titulo'),
    'seccion': fields.Integer(description='Numero de seccion'),   
    'asistio': fields.Integer(description='Si asistio'),
})

page_of_asistencia = api.inherit('Page of asistencia', pagination, {
    'items': fields.List(fields.Nested(asistencia))
})


acta_monitor = api.model('acta_monitor', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the acta_monitor'),
    'id_monitor': fields.Integer(attribute='monitor.id'),
    'nombre_monitor': fields.String(attribute='monitor.nombre'),
    'apellido_monitor' : fields.String(attribute='monitor.apellido'),
    'id_estudiante': fields.Integer(attribute='estudiante.id'),
    'nombre_estudiante': fields.String(attribute='estudiante.usuario.nombre'),
    'apellido_estudiante': fields.String(attribute='estudiante.usuario.apellido'),
    'empresa_estudiante': fields.String(attribute='estudiante.usuario.empresa'),
    'telefono_estudiante': fields.String(attribute='estudiante.usuario.telefono'),
    'email_estudiante': fields.String(attribute='estudiante.usuario.email'),
    'empresa_estudiante': fields.String(attribute='estudiante.empresa'),
    'empresa' : fields.String(required=True, description="Empresa"),
    'meet' : fields.String(required=True, description="Meet"),
    'actividad' : fields.String(required=True, description="Actividad"),
    'tema' : fields.String(required=True, description="Tema"),
    'resumen' : fields.String(required=True, description="Resumen"),
    'acuerdos' : fields.String(required=True, description="Acuerdos"),
    'observaciones' : fields.String(required=True, description="Observaciones"),
    'evidencia' : fields.String(required=True, description="Evidencia"),
    'fecha' : fields.Date(required=False, description="Fecha y hora")
})

page_of_acta_monitor = api.inherit('Page of acta_monitor', pagination, {
    'items': fields.List(fields.Nested(acta_monitor))
})


curso_profesor = api.model('curso_profesor', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the user and rol'),
    'id_curso': fields.Integer(attribute='curso.id'),
    'id_profesor': fields.Integer(attribute='profesor.id'),
    'id_grupo': fields.Integer(attribute='grupo.id'),
    'grupo': fields.String(attribute='grupo.descripcion'),
    'titulo': fields.String(attribute='curso.titulo'),
    'url': fields.String(attribute='curso.url'),
    'id_coordinador': fields.Integer(attribute='curso.id_coordinador'),
    'coordinador_profesor': fields.String(attribute='curso.coordinador.nombre'),
    'coordinador_profesor_apellido': fields.String(attribute='curso.coordinador.apellido'),
    'nombre_usuario': fields.String(attribute='profesor.nombre'),
    'apellido_usuario': fields.String(attribute='profesor.apellido'),

})

page_of_curso_profesor = api.inherit('Page of usuario_rol', pagination, {
    'items': fields.List(fields.Nested(curso_profesor))
})


acta_docente = api.model('acta_docente', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the acta_docente'),    
    'meet' : fields.String(required=True, description="Meet"),
    'seccion': fields.Integer(description='Numero de seccion'),
    'observaciones' : fields.String(required=True, description="Observaciones"),
    'evidencia' : fields.String(required=True, description="Evidencia"),
    'id_curso_profesor': fields.Integer(attribute='curso_docente.id')    
})

page_of_acta_docente = api.inherit('Page of acta_docente', pagination, {
    'items': fields.List(fields.Nested(acta_docente))
})

resource_fields = api.model('Resource', {
    'name': fields.String,
})

canvas = api.model('canvas', {
    'id': fields.Integer(readOnly=True, description='Clave para identificar el canvas'),
    'contenido': fields.String(required=True, description='Nombre contenido'),
    'id_usuario': fields.Integer(attribute='usuario.id',description='identificador usuario'),
    'nombre_usuario': fields.String(attribute='usuario.nombre',description='nombre usuario'),
    'apellido_usuario': fields.String(attribute='usuario.apellido',description='apellido usuario'),
    'telefono_usuario': fields.String(attribute='usuario.telefono',description='telefono usuario'),
    'estado': fields.String(description='estado'),

})

page_of_canvas = api.inherit('Page of canvas', pagination, {
    'items': fields.List(fields.Nested(canvas))
})


estado = api.model('estado', {
    'id': fields.Integer(readOnly=True, description='Id de estado'),
    'estado': fields.String(required=True, description='Estado de encuesta')
})


categoria = api.model('categoria', {
    'id': fields.Integer(readOnly=True, description='Id categoria'),
    'nombre': fields.String(required=True, description='Nombre de la categoria')
})


calificacion = api.model('calificacion', {
    'id': fields.Integer(readOnly=True, description='Id calificaciones'),
    'calificacion': fields.String(required=True, description='calificacion')
})


asesorias = api.model('asesorias', {
    'id': fields.Integer(readOnly=True, description='Clave primaria de la tabla asesorias'),
    'id_estudiante': fields.Integer(attribute='estudiante.id',description='identificador del usuario encuestado'),
    'estudiante_nombre': fields.String(attribute='estudiante.nombre', description='Nombre del usuario encuestado'),
    'estudiante_apellido': fields.String(attribute='estudiante.apellido', description='Apellido del usuario encuestado'),    
    'id_asesor': fields.Integer(attribute='asesor.id',description='Identificador del usuario encuestador'),
    'asesor_nombre': fields.String(attribute='asesor.nombre',description='Nombre del usuario encuestador'),
    'asesor_apellido': fields.String(attribute='asesor.apellido',description='Apellido del usuario encuestador')
})


encuesta = api.model('encuesta', {
    'id': fields.Integer(readOnly=True, description='Clave primaria de la tabla encuestas'),
    'codigo': fields.String(required=True, description='Codigo de la encuesta'),
    'fecha_creacion': fields.String(description='Fecha de creacion'),
    'fecha_actualizacion': fields.String(description='Fecha de creacion'),
    'asesorias_id': fields.Integer(attribute='asesoria.id'),
    'encuestado_id': fields.Integer(attribute='asesoria.id_estudiante'),
    'encuestado_nombre': fields.String(attribute='asesoria.estudiante.nombre'),
    'encuestado_apellido': fields.String(attribute='asesoria.estudiante.apellido'),
    'encuestador_id': fields.Integer(attribute='asesoria.id_asesor'),
    'encuestador_nombre': fields.String(attribute='asesoria.asesor.nombre'),
    'encuestador_apellido': fields.String(attribute='asesoria.asesor.apellido'),
    'estado_id': fields.Integer(required=True, attribute='estado.id'),
    'estado': fields.String(attribute='estado.estado'),
    'observacion': fields.String(description='Observación'),
    'evidencia' : fields.String(required=False, description="Evidencia")
})


preguntas = api.model('preguntas', {
    'id': fields.Integer(readOnly=True, description='Clave primaria de la tabla preguntas'),
    'pregunta': fields.String(required=True, descripcion='Pregunta a realizar'),
    'categoria_id': fields.Integer(atribute='categoria.id', required=True),
    'categoria': fields.String(attribute='categoria.nombre')
})


respuestas = api.model('respuestas', {
    'id': fields.Integer(readOnly=True, description='Clave primaria de la tabla preguntas'),
    'pregunta_id': fields.Integer(attribute='pregunta.id', required=True),
    'pregunta': fields.String(attribute='pregunta.pregunta'),
    'encuesta_id': fields.Integer(attribute='encuesta.id'),    
    'respuesta': fields.String(required=True, description='Respuesta por el encuestado'),
    'observaciones': fields.String(required=True, description='Observaciones hechas por el encuestador'),
    'calificacion_id': fields.Integer(attribute='calificacion.id', required=True),
    'calificacion': fields.String(attribute='calificacion.calificacion'),
    'fecha': fields.String(descripcion='Fecha de registro de la respuesta')
})