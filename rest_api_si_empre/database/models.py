from datetime import datetime
from sqlalchemy import DateTime, Boolean
from rest_api_si_empre.database import db
import hashlib 
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_bcrypt import generate_password_hash

class tbl_roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(128))

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __repr__(self):
        return '<tbl_roles %r>' % self.descripcion


class Tbl_grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(128))

    def __init__(self,descripcion):
        self.descripcion = descripcion
    
    def __repr__(self):
        return '<Tbl_grupo %r>' % self.descripcion


class Tbl_cv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grado_academico = db.Column(db.String(128))
    postgrado = db.Column(db.String(128))
    profesion = db.Column(db.String(128))
    id_usuario = db.Column(db.Integer, db.ForeignKey('tbl_usuario.id'))
    usuario = db.relationship('tbl_usuario', backref=db.backref('tbl_cv', lazy='dynamic'))
    cv_lac = db.Column(db.String(128))
    perfil = db.Column(db.String(512))
    experiencia = db.Column(db.Text)
    area_con = db.Column(db.Text)
    curso_dicta = db.Column(db.Text)


    def __init__(self,grado_academico,postgrado,profesion,usuario,cv_lac,perfil,experiencia,area_con,curso_dicta):
        self.grado_academico = grado_academico
        self.postgrado = postgrado
        self.profesion = profesion
        self.usuario = usuario
        self.cv_lac = cv_lac
        self.perfil = perfil
        self.experiencia = experiencia
        self.area_con = area_con
        self.curso_dicta = curso_dicta

    def __repr__(self):
        return '<Tbl_cv %r>' % self.grado_academico

class Tbl_franja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<Tbl_franja %r>' % self.nombre



class tbl_contenido_curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text) 
    id_curso = db.Column(db.Integer, db.ForeignKey('tbl_curso_profesor.id'))
    curso = db.relationship('tbl_curso_profesor', backref=db.backref('tbl_contenido_curso', lazy='dynamic'))

    def __init__(self, contenido, curso):
        self.contenido = contenido
        self.curso = curso

    def __repr__(self):
        return '<tbl_contenido_curso %r>' % self.curso

class tbl_subsector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(512))
  
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<tbl_subsector %r>' % self.nombre

class Tbl_estudiantes(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    activo = db.Column(db.Boolean)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tbl_usuario.id'))
    usuario = db.relationship('tbl_usuario', foreign_keys=[id_usuario])
    empresa = db.Column(db.String(128))
    barrio_p = db.Column(db.String(128))
    comuna_p = db.Column(db.String(128))
    corregimiento_p = db.Column(db.String(128))
    id_subsector = db.Column(db.Integer, db.ForeignKey('tbl_subsector.id'))
    subsector = db.relationship('tbl_subsector', foreign_keys=[id_subsector])
    actividad_e = db.Column(db.String(512))
    direccion_e = db.Column(db.String(128))
    barrio_e = db.Column(db.String(128))
    comuna_e = db.Column(db.String(128))
    corregimiento_e = db.Column(db.String(128))
    num_whatsapp = db.Column(db.String(10))
    facebook = db.Column(db.String(128))
    instagram = db.Column(db.String(128))
    pagina_web = db.Column(db.String(128))
    otra_red_social = db.Column(db.String(128))
    num_movil_e = db.Column(db.String(10))
    num_emp = db.Column(db.Integer)
    ano_fun = db.Column(db.Integer)
    per_emp = db.Column(db.String(128))
    certificado = db.Column(db.String(256))

    def __init__(self, latitud, longitud, activo, usuario, empresa, barrio_p, comuna_p, corregimiento_p, subsector, actividad_e, direccion_e, barrio_e, comuna_e, corregimiento_e, num_whatsapp, facebook, instagram, pagina_web, otra_red_social, num_movil_e,num_emp,ano_fun,per_emp, certificado):
        self.latitud = latitud
        self.longitud = longitud
        self.activo = activo
        self.usuario = usuario
        self.empresa = empresa
        self.barrio_p = barrio_p
        self.comuna_p = comuna_p
        self.corregimiento_p = corregimiento_p
        self.subsector = subsector
        self.actividad_e = actividad_e
        self.direccion_e = direccion_e
        self.barrio_e = barrio_e
        self.comuna_e = comuna_e
        self.corregimiento_e = corregimiento_e
        self.num_whatsapp = num_whatsapp
        self.facebook = facebook
        self.instagram = instagram
        self.pagina_web = pagina_web
        self.otra_red_social = otra_red_social
        self.num_movil_e = num_movil_e
        self.num_emp = num_emp
        self.ano_fun = ano_fun
        self.per_emp = per_emp
        self.certificado = certificado


    def __repr__(self):
        return '<Tbl_estudiantes %r>' % self.usuario


def encrypt_string(hash_string):
    if len(hash_string) < 20:
        password_hash = \
        hashlib.sha256(hash_string.encode()).hexdigest()
        return password_hash
    else:
        return hash_string


class tbl_usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    apellido = db.Column(db.String(128))
    username = db.Column(db.String(164))
    password_hash = db.Column(db.String(128))
    identificacion = db.Column(db.String(11))
    email = db.Column(db.String(64))
    direccion = db.Column(db.String(128))
    telefono = db.Column(db.String(10))
    estado = db.Column(db.Boolean)
    delete = db.Column(db.Boolean)

    
        
    def __init__(self, nombre, apellido, username, password_hash, identificacion, email, direccion, telefono, estado, delete):
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.password_hash = encrypt_string(password_hash)
        self.identificacion = identificacion
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.estado =  estado
        self.delete =  delete

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def is_admin(self):
        return self.admin



class tbl_curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128), nullable=False)
    descripcion = db.Column(db.String(512), nullable=False)
    objetivo = db.Column(db.String(512), nullable=False)      
    url = db.Column(db.String(256), nullable=False)
    id_coordinador = db.Column(db.Integer, db.ForeignKey('tbl_usuario.id'))
    coordinador = db.relationship('tbl_usuario', foreign_keys=[id_coordinador])    


    def __init__(self, titulo, descripcion, objetivo, url, coordinador):
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivo = objetivo
        self.url = url
        self.coordinador = coordinador        

    def __repr__(self):
        return '<tbl_curso %r>' % self.titulo


class Tbl_usuario_rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tbl_usuario.id'))
    id_rol = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))
    usuario = db.relationship(tbl_usuario, backref='paths4')
    rol = db.relationship(tbl_roles, backref='paths4')

    def to_json(self):
        return dict(
            id = self.id,
            id_usuario = self.id_usuario,
            id_rol = self.id_rol,
        )

    def __init__(self, usuario, rol):
        self.usuario = usuario
        self.rol = rol

    def __repr__(self):
        return '<Tbl_usuario_rol %r>' % self.id_usuario


class tbl_curso_profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_curso = db.Column(db.Integer, db.ForeignKey('tbl_curso.id'))
    id_profesor = db.Column(db.Integer, db.ForeignKey('tbl_usuario.id'))
    id_grupo = db.Column(db.Integer, db.ForeignKey(Tbl_grupo.id))
    curso = db.relationship('tbl_curso', foreign_keys=[id_curso])
    profesor = db.relationship('tbl_usuario', foreign_keys=[id_profesor])
    grupo = db.relationship(Tbl_grupo, backref='paths8')

    def __init__(self, curso, profesor, grupo):
        self.curso = curso
        self.profesor = profesor
        self.grupo = grupo
    
    def __repr__(self):
        return '<tbl_curso_profesor %r>' % self.id

class Tbl_programacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seccion = db.Column(db.Integer)
    id_curso = db.Column(db.Integer, db.ForeignKey(tbl_curso_profesor.id))
    id_franja = db.Column(db.Integer, db.ForeignKey(Tbl_franja.id))
    curso = db.relationship(tbl_curso_profesor, backref='paths')
    franja = db.relationship(Tbl_franja, backref='paths')
    meet = db.Column(db.String(128), nullable=False)
    fecha = db.Column(db.String(128), nullable=False)


    def __init__(self, curso, franja, seccion, meet, fecha):
        self.curso = curso        
        self.franja = franja
        self.seccion = seccion
        self.meet = meet
        self.fecha = fecha


    def __repr__(self):
        return '<Tbl_programacion %r>' % self.id


class Tbl_estudiante_grupo_curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey(Tbl_estudiantes.id))
    id_grupo = db.Column(db.Integer, db.ForeignKey(Tbl_grupo.id))
    id_curso = db.Column(db.Integer, db.ForeignKey(tbl_curso_profesor.id))
    estudiante = db.relationship(Tbl_estudiantes, backref='paths1')
    grupo = db.relationship(Tbl_grupo, backref='paths1')
    curso = db.relationship(tbl_curso_profesor, backref='paths1')


    def to_json(self):
        return dict(
            id = self.id,
            id_estudiante = self.id_estudiante,
            id_grupo = self.id_grupo,
            id_curso = self.id_curso,
        )

    def __init__(self,estudiante,grupo,curso):
        self.estudiante = estudiante
        self.grupo = grupo
        self.curso = curso

    def __repr__(self):
        return '<Tbl_estudiante_grupo_curso %r>' % self.id


class Tbl_monitorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_monitor = db.Column(db.Integer, db.ForeignKey(tbl_usuario.id))
    id_estudiante = db.Column(db.Integer, db.ForeignKey(Tbl_estudiantes.id))
    id_grupo = db.Column(db.Integer, db.ForeignKey(Tbl_grupo.id))
    monitor = db.relationship(tbl_usuario, backref='paths2')
    estudiante = db.relationship(Tbl_estudiantes, backref='paths2')
    grupo = db.relationship(Tbl_grupo, backref='paths2')

    def __init__(self, monitor, estudiante, grupo):
        self.monitor = monitor
        self.estudiante = estudiante
        self.grupo = grupo
    
    def __repr__(self):
        return '<Tbl_monitorias %r>' % self.id



class Tbl_mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey(Tbl_estudiantes.id))
    id_usuario = db.Column(db.Integer, db.ForeignKey(tbl_usuario.id))
    created = db.Column(db.DateTime, default=datetime.now())    
    mensaje = db.Column(db.String(1024), nullable=False)
    usuario = db.relationship(tbl_usuario, backref='paths')
    estudiante = db.relationship(Tbl_estudiantes, backref='paths')
    

    def __init__(self, mensaje, estudiante, usuario):
        self.mensaje = mensaje
        self.estudiante = estudiante
        self.usuario = usuario    
    
    def __repr__(self):
        return '<Tbl_mensaje %r>' % self.id

        
class Tbl_asistencia(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey(Tbl_estudiantes.id))
    id_curso = db.Column(db.Integer, db.ForeignKey(tbl_curso_profesor.id))
    seccion = db.Column(db.Integer)
    estudiante = db.relationship('Tbl_estudiantes', foreign_keys=[id_estudiante])
    curso = db.relationship('tbl_curso_profesor', foreign_keys=[id_curso])
    asistio = db.Column(db.Integer)

    def __init__(self,estudiante,curso,seccion,asistio):
        self.estudiante = estudiante
        self.curso = curso
        self.seccion = seccion
        self.asistio = asistio

    def __repr__(self):
        return '<Tbl_asistencia %r>' % self.id


class Tbl_acta_monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    id_monitor = db.Column(db.Integer, db.ForeignKey(tbl_usuario.id))
    id_estudiante = db.Column(db.Integer, db.ForeignKey(Tbl_estudiantes.id))
    monitor = db.relationship(tbl_usuario, backref='paths5')
    estudiante = db.relationship(Tbl_estudiantes, backref='paths5')
    empresa = db.Column(db.String(128), nullable=False)
    meet = db.Column(db.String(128), nullable=False)
    actividad = db.Column(db.String(64), nullable=False)
    tema = db.Column(db.String(512), nullable=False)
    resumen = db.Column(db.String(2024), nullable=False)
    acuerdos = db.Column(db.String(2024), nullable=False)
    observaciones = db.Column(db.String(1024), nullable=False)
    evidencia = db.Column(db.String(128), nullable=False)


    def __init__(self, monitor, estudiante, empresa,meet,actividad,tema,resumen,acuerdos,observaciones,evidencia):
        self.monitor = monitor
        self.estudiante = estudiante
        self.empresa = empresa
        self.meet = meet
        self.actividad = actividad
        self.tema = tema
        self.resumen = resumen
        self.acuerdos = acuerdos
        self.observaciones = observaciones
        self.evidencia = evidencia
        
    
    def __repr__(self):
        return '<Tbl_acta_monitor %r>' % self.id





class Tbl_acta_docente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meet = db.Column(db.String(128), nullable=False)
    seccion = db.Column(db.Integer)
    observaciones = db.Column(db.String(1024), nullable=False)
    evidencia = db.Column(db.String(128), nullable=False) 
    id_curso_profesor = db.Column(db.Integer, db.ForeignKey(tbl_curso_profesor.id)) 
    curso_docente = db.relationship(tbl_curso_profesor, backref='paths89')
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __init__(self, meet, seccion, observaciones, evidencia, curso_docente):        
        self.meet = meet
        self.seccion = seccion
        self.observaciones = observaciones
        self.evidencia = evidencia
        self.curso_docente = curso_docente
        
    
    def __repr__(self):
        return '<Tbl_acta_docente %r>' % self.id


class tbl_canvas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text) 
    id_usuario = db.Column(db.Integer, db.ForeignKey('tbl_usuario.id'))
    usuario = db.relationship('tbl_usuario', backref=db.backref('tbl_canvas', lazy='dynamic'))
    estado = db.Column(db.String(64))

    def __init__(self, contenido, usuario, estado):
        self.contenido = contenido
        self.usuario = usuario
        self.estado = estado

    def __repr__(self):
        return '<tbl_canvas %r>' % self.id

class tbl_estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(32), nullable=False)


    def __init__(self, estado):
        self.estado = estado

    def __repr__(self):
        return '<tbl_estado %r>' % self.id



class tbl_categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(32), nullable=False)

    def __init__(self, estado):
        self.nombre = nombre

    def __repr__(self):
        return '<tbl_categoria %r>' % self.id



class tbl_calificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.String(256), nullable=False)

    def __init__(self, calificacion):
        self.calificacion = calificacion

    def __repr__(self):
        return '<tbl_calificacion %r>' % self.id




class tbl_asesorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey(tbl_usuario.id))
    id_asesor = db.Column(db.Integer, db.ForeignKey(tbl_usuario.id))
    estudiante = db.relationship('tbl_usuario', foreign_keys=[id_estudiante])
    asesor = db.relationship('tbl_usuario', foreign_keys=[id_asesor])

    def __init__(self, estudiante, asesor):
        self.estudiante = estudiante
        self.asesor = asesor

    
    def __repr__(self):
        return '<tbl_asesorias %r>' % self.id


class tbl_encuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(16), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    asesorias_id = db.Column(db.Integer, db.ForeignKey(tbl_asesorias.id))
    asesoria = db.relationship('tbl_asesorias', foreign_keys=[asesorias_id])
    estado_id = db.Column(db.Integer, db.ForeignKey(tbl_estado.id)) 
    estado = db.relationship(tbl_estado, backref='paths10')
    observacion = db.Column(db.String(1024), default="")
    evidencia = db.Column(db.String(128), nullable=False)
    validacion = db.Column(db.Boolean)

    def __init__(self, codigo, asesoria, estado, evidencia, validacion):
        self.codigo = codigo
        self.asesoria = asesoria
        self.estado = estado        
        self.evidencia = evidencia
        self.validacion = validacion
    
    def __repr__(self):
        return '<tbl_encuesta %r>' % self.id


    
class tbl_preguntas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.String(1024), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey(tbl_categoria.id)) 
    categoria = db.relationship(tbl_categoria, backref='paths11')

    def __init__(self, pregunta, categoria):
        self.pregunta = pregunta
        self.categoria = categoria

    def __repr__(self):
        return '<tbl_preguntas %r>' % self.id



class tbl_respuestas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer, db.ForeignKey(tbl_preguntas.id))
    pregunta = db.relationship(tbl_preguntas, backref='paths12')
    encuesta_id = db.Column(db.Integer, db.ForeignKey(tbl_encuesta.id))
    encuesta = db.relationship(tbl_encuesta, backref='paths12')
    respuesta = db.Column(db.String(1024), nullable=False)
    observaciones = db.Column(db.String(1024), nullable=False)
    calificacion_id = db.Column(db.Integer, db.ForeignKey(tbl_calificacion.id))
    calificacion = db.relationship(tbl_calificacion, backref='paths12')
    fecha = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, pregunta, encuesta, respuesta, observaciones, calificacion):
        self.pregunta = pregunta
        self.encuesta = encuesta
        self.respuesta = respuesta
        self.observaciones = observaciones
        self.calificacion = calificacion

    
    def __repr__(self):
        return '<tbl_respuesta %r>' % self.id

