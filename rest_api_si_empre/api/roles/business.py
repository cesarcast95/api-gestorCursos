from rest_api_si_empre.database.models import tbl_roles, Tbl_franja, Tbl_estudiantes, tbl_usuario, tbl_curso, Tbl_grupo, Tbl_cv, Tbl_estudiante_grupo_curso, Tbl_programacion, Tbl_usuario_rol, Tbl_monitorias, Tbl_asistencia,Tbl_acta_monitor, tbl_contenido_curso, Tbl_mensaje, tbl_curso_profesor,Tbl_acta_docente, encrypt_string, tbl_canvas, tbl_subsector
from rest_api_si_empre.database.models import tbl_asesorias, tbl_estado, tbl_encuesta, tbl_categoria, tbl_preguntas, tbl_respuestas, tbl_calificacion
from rest_api_si_empre.database import db
from sqlalchemy import exc
from datetime import datetime
from datetime import datetime


def create_roles_roles(data):
    descripcion = data.get('descripcion')     
    roles = tbl_roles(descripcion)
    db.session.add(roles)
    db.session.commit()


def update_roles(rol_id, data):
    rol = tbl_roles.query.filter(tbl_roles.id == rol_id).one()
    rol.descripcion = data.get('descripcion')
    db.session.add(rol)
    db.session.commit()


def delete_roles(rol_id):
    rol = tbl_roles.query.filter(tbl_roles.id == rol_id).one()
    db.session.delete(rol)
    db.session.commit()


def create_group(data):
    descripcion = data.get('descripcion')
    group_id = data.get('id')

    group = Tbl_grupo(descripcion)
    if group_id:
        group.id = group_id

    db.session.add(group)
    db.session.commit()


def update_group(group_id, data):
    group = Tbl_grupo.query.filter(Tbl_grupo.id == group_id).one()
    group.descripcion = data.get('descripcion')
    db.session.add(group)
    db.session.commit()


def delete_group(group_id):
    group = Tbl_grupo.query.filter(Tbl_grupo.id == group_id).one()
    db.session.delete(group)
    
def create_franja(data):
    nombre = data.get('nombre')
    franja = Tbl_franja(nombre)
    db.session.add(franja)
    db.session.commit()

def delete_franja(franja_id):
    franja = Tbl_franja.query.filter(Tbl_franja.id == franja_id).one()
    db.session.delete(franja)
    db.session.commit()

def update_franja(franja_id, data):
    franja = Tbl_franja.query.filter(Tbl_franja.id == franja_id).one()
    franja.nombre= data.get('nombre')
    db.session.add(franja)
    db.session.commit()

def create_subsector(data):
    nombre = data.get('nombre')
    subsector = tbl_subsector(nombre)
    db.session.add(subsector)
    db.session.commit()

def delete_subsector(subsector_id):
    subsector = tbl_subsector.query.filter(tbl_subsector == subsector_id).one()
    db.session.delete(subsector)
    db.session.commit()

def update_subsector(subsector_id, data):
    subsector = tbl_subsector.query.filter(tbl_subsector.id == subsector_id).one()
    subsector.nombre = data.get('nombre')
    db.session.add(subsector)
    db.session.commit()

def create_estudiante(data):
    latitud = data.get('latitud')
    longitud = data.get('longitud')
    activo = data.get('activo')
    id_usuario = data.get('id_usuario')
    usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()
    empresa= data.get('empresa')
    barrio_p = data.get('barrio_p')
    comuna_p = data.get('comuna_p')
    corregimiento_p = data.get('corregimiento_p')
    id_subsector = data.get('id_subsector')
    subsector = tbl_subsector.query.filter(tbl_subsector.id == id_subsector).one()
    actividad_e = data.get('actividad_e')
    direccion_e = data.get('direccion_e')
    barrio_e = data.get('barrio_e')
    comuna_e = data.get('comuna_e')
    corregimiento_e = data.get('corregimiento_e')
    num_whatsapp = data.get('num_whatsapp')
    facebook = data.get('facebook')
    instagram = data.get('instagram')
    pagina_web = data.get('pagina_web')
    otra_red_social = data.get('otra_red_social')
    num_movil_e = data.get('num_movil_e')
    num_emp = data.get('num_emp')
    ano_fun = data.get('ano_fun')
    per_emp = data.get('per_emp')
    certificado = data.get('certificado')
    
    estudiante = Tbl_estudiantes(latitud, longitud, activo, usuario, empresa, barrio_p, comuna_p, corregimiento_p, subsector, actividad_e, direccion_e, barrio_e, comuna_e, corregimiento_e, num_whatsapp, facebook, instagram, pagina_web, otra_red_social, num_movil_e,num_emp,ano_fun,per_emp, certificado)
    try:
        db.session.add(estudiante)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403       
    

def delete_estudiante(estudiante_id):
    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == estudiante_id).one()
    db.session.delete(estudiante)
    db.session.commit()


def update_estudiante(estudiante_id, data):
    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == estudiante_id).one()
    estudiante.latitud = data.get('latitud')
    estudiante.longitud = data.get('longitud')
    estudiante.activo = data.get('activo')
    id_usuario = data.get('id_usuario')
    estudiante.usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one() 
    estudiante.empresa= data.get('empresa') 
    estudiante.barrio_p = data.get('barrio_p')
    estudiante.comuna_p = data.get('comuna_p')
    estudiante.corregimiento_p = data.get('corregimiento_p')
    id_subsector = data.get('id_subsector')
    estudiante.subsector = tbl_subsector.query.filter(tbl_subsector.id == id_subsector).one()
    estudiante.actividad_e = data.get('actividad_e')
    estudiante.direccion_e = data.get('direccion_e')
    estudiante.barrio_e = data.get('barrio_e')
    estudiante.comuna_e = data.get('comuna_e')
    estudiante.corregimiento_e = data.get('corregimiento_e')
    estudiante.num_whatsapp = data.get('num_whatsapp')
    estudiante.facebook = data.get('facebook')
    estudiante.instagram = data.get('instagram')
    estudiante.pagina_web = data.get('pagina_web')
    estudiante.otra_red_social = data.get('otra_red_social')
    estudiante.num_movil_e = data.get('num_movil_e')
    estudiante.num_emp = data.get('num_emp')
    estudiante.ano_fun = data.get('ano_fun')
    estudiante.per_emp = data.get('per_emp')
    estudiante.certificado = data.get('certificado')
    db.session.add(estudiante)
    db.session.commit()


def create_usuario(data):
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    username = data.get('username')
    password_hash = data.get('password_hash')
    identificacion = data.get('identificacion')
    email = data.get('email')
    direccion = data.get('direccion')
    telefono = data.get('telefono')
    estado = data.get('estado')
    delete = data.get('delete')
    usuario = tbl_usuario(nombre, apellido, username, password_hash, identificacion, email, direccion, telefono, estado, delete)
   
    db.session.add(usuario)
    db.session.commit()
    return usuario.id

def delete_usuario(usuario_id):
    usuario = tbl_usuario.query.filter(tbl_usuario.id == usuario_id).one()
    usuario.delete = 1
    db.session.add(usuario)
    db.session.commit()

def update_usuario(usuario_id, data):
    usuario = tbl_usuario.query.filter(tbl_usuario.id == usuario_id).one()
    usuario.nombre= data.get('nombre')
    usuario.apellido = data.get('apellido')
    usuario.username = data.get('username')
    usuario.password_hash = encrypt_string(data.get('password_hash'))
    usuario.identificacion = data.get('identificacion')
    usuario.email = data.get('email')
    usuario.direccion = data.get('direccion')
    usuario.telefono = data.get('telefono')
    usuario.estado = data.get('estado')
    usuario.delete = data.get('delete')
    db.session.add(usuario)
    db.session.commit()


def create_roles_curso(data):
    titulo = data.get('titulo')
    descripcion = data.get('descripcion')
    objetivo = data.get('objetivo')
    url = data.get('url')
    id_coordinador = data.get('id_coordinador')
    coordinador = tbl_usuario.query.filter(tbl_usuario.id == id_coordinador).one()
    curso = tbl_curso(titulo, descripcion, objetivo, url, coordinador)
    db.session.add(curso)
    db.session.commit()


def update_curso(curso_id, data):
    curso = tbl_curso.query.filter(tbl_curso.id == curso_id).one()
    curso.titulo = data.get('titulo')
    curso.descripcion = data.get('descripcion')
    curso.objetivo = data.get('objetivo')
    curso.url = data.get('url')
    id_coordinador = data.get('id_coordinador')
    curso.coordinador = tbl_usuario.query.filter(tbl_usuario.id == id_coordinador).one()    
    db.session.add(curso)
    db.session.commit()


def delete_curso(curso_id):
    curso = tbl_curso.query.filter(tbl_curso.id == curso_id).one()
    db.session.delete(curso)
    db.session.commit()

def create_contenido(data):# cambio de tabla, apuntar a curso_profesor
    contenido = data.get('contenido')
    id_curso = data.get('id_curso')
    curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()
    con = tbl_contenido_curso(contenido, curso)
    db.session.add(con)
    db.session.commit()


def update_contenido(contenido_id, data):
    con = tbl_contenido_curso.query.filter(tbl_contenido_curso.id == contenido_id).one()
    con.contenido = data.get('contenido')
    id_curso = data.get('id_curso')
    con.curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()  
    db.session.add(con)
    db.session.commit()


def delete_contenido(contenido_id):
    con = tbl_contenido_curso.query.filter(tbl_contenido_curso.id == contenido_id).one()
    db.session.delete(con)
    db.session.commit()


def create_cv(data):
    grado_academico = data.get('grado_academico')
    postgrado = data.get('postgrado')
    profesion = data.get('profesion')
    id_usuario = data.get('id_usuario')
    cv_lac = data.get('cv_lac')
    perfil = data.get('perfil')
    experiencia = data.get('experiencia')
    area_con = data.get('area_con')
    curso_dicta = data.get('curso_dicta')
    usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()
    tbl_cv = Tbl_cv(grado_academico, postgrado, profesion, usuario, cv_lac, perfil,experiencia, area_con, curso_dicta)
    db.session.add(tbl_cv)
    db.session.commit()


def update_cv(cv_id, data):
    cv = Tbl_cv.query.filter(Tbl_cv.id_usuario == cv_id).one()
    cv.grado_academico = data.get('grado_academico')
    cv.postgrado = data.get('postgrado')
    cv.profesion = data.get('profesion')
    id_usuario = data.get('id_usuario')
    cv.cv_lac = data.get('cv_lac')
    cv.perfil = data.get('perfil')
    cv.experiencia = data.get('experiencia')
    cv.area_con = data.get('area_con')
    cv.curso_dicta = data.get('curso_dicta')
    cv.usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()
    db.session.add(cv)
    db.session.commit()


def delete_cv(cv_id):
    cv = Tbl_cv.query.filter(Tbl_cv.id == cv_id).one()
    db.session.delete(cv)
    db.session.commit()


def create_estudiante_grupo_curso(data):
    id_estudiante = data.get('id_estudiante')
    id_grupo = data.get('id_grupo')
    id_curso = data.get('id_curso')
    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    grupo = Tbl_grupo.query.filter(Tbl_grupo.id == id_grupo).one()

    curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()
    estudiante_grupo_curso = Tbl_estudiante_grupo_curso(estudiante,grupo,curso)

    try:
        db.session.add(estudiante_grupo_curso)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403

def update_estudiante_grupo_curso(e_g_c_id,data):
    e_g_c = Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id == e_g_c_id).one()
    id_estudiante = data.get('id_estudiante')
    id_grupo = data.get('id_grupo')
    id_curso = data.get('id_curso')
    e_g_c.estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    e_g_c.grupo = Tbl_grupo.query.filter(Tbl_grupo.id == id_grupo).one()
    e_g_c.curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()
    try:
        db.session.add(e_g_c)
        db.session.commit()
        return 204
    except exc.OperationalError:
        db.session.rollback()
        return 403


    

def delete_estudiante_grupo_curso(estudiante_grupo_curso_id):
    estudiante_grupo_curso = Tbl_estudiante_grupo_curso.query.filter(Tbl_estudiante_grupo_curso.id == estudiante_grupo_curso_id).one()
    db.session.delete(estudiante_grupo_curso)


def create_programacion(data):
    id_curso = data.get('id_curso')
    curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()
    id_franja = data.get('id_franja')
    franja = Tbl_franja.query.filter(Tbl_franja.id == id_franja).one()
    seccion = data.get('seccion')
    meet = data.get('meet')
    fecha = data.get('fecha')
    programacion = Tbl_programacion(curso, franja, seccion, meet, fecha)
    db.session.add(programacion)
    db.session.commit()


def update_programacion(programacion_id, data):    
    programacion = Tbl_programacion.query.filter(Tbl_programacion.id == programacion_id).one()
    id_curso = data.get('id_curso')
    programacion.curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()
    id_franja = data.get('id_franja')
    programacion.franja = Tbl_franja.query.filter(Tbl_franja.id == id_franja).one()
    programacion.seccion = data.get('seccion')
    programacion.meet = data.get('meet')
    programacion.fecha = data.get('fecha')  
    db.session.add(programacion)
    db.session.commit()

    
    try:
        db.session.add(programacion)
        db.session.commit()
        return 204
    except  exc.OperationalError:
        db.session.rollback()
        return 403


def delete_programacion(programacion_id):
    programacion = Tbl_programacion.query.filter(Tbl_programacion.id == programacion_id).one()
    db.session.delete(programacion)


def create_usuario_rol(data):
    id_usuario = data.get('id_usuario')
    id_rol = data.get('id_rol')
    usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()
    rol = tbl_roles.query.filter(tbl_roles.id == id_rol).one()
    usuario_rol = Tbl_usuario_rol(usuario, rol)

    try:
        db.session.add(usuario_rol)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403


def update_usuario_rol(usuario_rol_id, data):
    usuario_rol = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id == usuario_rol_id).one()
    id_usuario = data.get('id_usuario')
    id_rol = data.get('id_rol')
    usuario_rol.usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()
    usuario_rol.rol = tbl_roles.query.filter(tbl_roles.id == id_rol).one() 
    
    try:
        db.session.add(usuario_rol)
        db.session.commit()
        return 204
    except  exc.OperationalError:
        db.session.rollback()
        return 403


def delete_usuario_rol(usuario_rol_id):
    usuario_rol = Tbl_usuario_rol.query.filter(Tbl_usuario_rol.id == usuario_rol_id).one()
    db.session.delete(usuario_rol)
    db.session.commit()

# sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) 
# (1644, 'No se puede ingresar más de 10 estudiantes por monitor')
def create_monitorias(data):
    id_monitor = data.get('id_monitor')
    monitor = tbl_usuario.query.filter(tbl_usuario.id == id_monitor).one()
    id_estudiante = data.get('id_estudiante')
    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    id_grupo = data.get('id_grupo')
    grupo = Tbl_grupo.query.filter(Tbl_grupo.id == id_grupo).one()
    monitorias = Tbl_monitorias(monitor, estudiante, grupo)
    try:
        db.session.add(monitorias)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403
    
        

def update_monitorias(monitorias_id, data):
    monitorias = Tbl_monitorias.query.filter(Tbl_monitorias.id == monitorias_id).one()
    id_monitor = data.get('id_monitor')
    id_estudiante = data.get('id_estudiante')
    id_grupo = data.get('id_grupo')
    monitorias.monitor = tbl_usuario.query.filter(tbl_usuario.id == id_monitor).one()
    monitorias.estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    monitorias.grupo = Tbl_grupo.query.filter(Tbl_grupo.id == id_grupo).one()

    try:
        db.session.add(monitorias)
        db.session.commit()
        return 204
    except exc.OperationalError:
        db.session.rollback()
        return 403

    
def create_mensajes(data):
    id_estudiante = data.get('id_estudiante')    
    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id_usuario == id_estudiante).one()    
    id_usuario = data.get('id_usuario')
    usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()

    mensaje = data.get('mensaje') 
    mensajes = Tbl_mensaje(mensaje, estudiante, usuario)
    db.session.add(mensajes)
    db.session.commit()


def update_mensajes(mensaje_id, data):
    mensajes = Tbl_mensaje.query.filter(Tbl_mensaje.id == mensaje_id).one()
    id_estudiante = data.get('id_estudiante')
    id_usuario = data.get('id_usuario')
    mensajes.mensaje = data.get('mensaje')
    mensajes.estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    mensajes.usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()    

    try:
        db.session.add(mensajes.usuario)
        db.session.commit()
        return 204
    except exc.OperationalError:
        db.session.rollback()
        return 403

        
def create_asistencia(data):
    id_estudiante = data.get('id_estudiante')
    id_curso = data.get('id_curso')
    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()
    seccion = data.get('seccion')
    asistio = data.get('asistio')
    asistencia = Tbl_asistencia(estudiante,curso,seccion,asistio)

    try:
        db.session.add(asistencia)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403

def update_asistencia(e_g_c_id,data):
    e_g_c = Tbl_asistencia.query.filter(Tbl_asistencia.id == e_g_c_id).one()
    id_estudiante = data.get('id_estudiante')
    id_curso = data.get('id_curso')
    e_g_c.estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    e_g_c.curso = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso).one()
    e_g_c.seccion = data.get('seccion')
    e_g_c.asistio = data.get('asistio')

    try:
        db.session.add(e_g_c)
        db.session.commit()
        return 204
    except exc.OperationalError:
        db.session.rollback()
        return 403

def delete_asistencia(asistencia_id):
    asistencia = Tbl_asistencia.query.filter(Tbl_asistencia.id == asistencia_id).one()
    db.session.delete(asistencia)


def create_acta_monitor(data):
    id_monitor = data.get('id_monitor')
    monitor = tbl_usuario.query.filter(tbl_usuario.id == id_monitor).one()
    id_estudiante = data.get('id_estudiante')
    estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    empresa = data.get('empresa')
    meet = data.get('meet')
    actividad = data.get('actividad')
    tema = data.get('tema')
    resumen = data.get('resumen')
    acuerdos = data.get('acuerdos')
    observaciones = data.get('observaciones')
    evidencia = data.get('evidencia')

    acta_monitor = Tbl_acta_monitor(monitor, estudiante, empresa,meet,actividad,tema,resumen,acuerdos,observaciones,evidencia)
    try:
        db.session.add(acta_monitor)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403

def update_acta_monitor(acta_id,data):
    acta_monitor = Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id==acta_id).one()
    id_monitor = data.get('id_monitor')
    acta_monitor.monitor = tbl_usuario.query.filter(tbl_usuario.id == id_monitor).one()
    id_estudiante = data.get('id_estudiante')
    acta_monitor.estudiante = Tbl_estudiantes.query.filter(Tbl_estudiantes.id == id_estudiante).one()
    acta_monitor.empresa = data.get('empresa')
    acta_monitor.meet = data.get('meet')
    acta_monitor.actividad = data.get('actividad')
    acta_monitor.tema = data.get('tema')
    acta_monitor.resumen = data.get('resumen')
    acta_monitor.acuerdos = data.get('acuerdos')
    acta_monitor.observaciones = data.get('observaciones')
    acta_monitor.evidencia = data.get('evidencia')
    db.session.add(acta_monitor)
    db.session.commit()


def delete_acta_monitor(id_acta_monitor):
    acta_monitor = Tbl_acta_monitor.query.filter(Tbl_acta_monitor.id==id_acta_monitor).one()
    db.session.delete(acta_monitor)
    db.session.commit()

def create_acta_docente(data):    
    id_curso_profesor = data.get('id_curso_profesor')
    curso_docente = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso_profesor).one()
    meet = data.get('meet')
    seccion = data.get('seccion')
    observaciones = data.get('observaciones')
    evidencia = data.get('evidencia')

    acta_docente = Tbl_acta_docente(meet, seccion, observaciones, evidencia, curso_docente)
    try:
        db.session.add(acta_docente)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403

def update_acta_docente(acta_id,data):
    acta_docente = Tbl_acta_docente.query.filter(Tbl_acta_docente.id==acta_id).one()
    id_curso_profesor = data.get('id_curso_profesor')
    acta_docente.curso_docente = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == id_curso_profesor).one()
    acta_docente.meet = data.get('meet')
    acta_docente.seccion = data.get('seccion')
    acta_docente.observaciones = data.get('observaciones')
    acta_docente.evidencia = data.get('evidencia')
    db.session.add(acta_docente)
    db.session.commit()

def delete_acta_docente(acta_id):
    acta_docente = Tbl_acta_docente.query.filter(Tbl_acta_docente.id==acta_id).one()
    db.session.delete(acta_docente)
    db.session.commit()


def create_curso_profesor(data):
    id_curso = data.get('id_curso')
    id_profesor = data.get('id_profesor')
    id_grupo = data.get('id_grupo')
    curso = tbl_curso.query.filter(tbl_curso.id == id_curso).one()
    profesor = tbl_usuario.query.filter(tbl_usuario.id == id_profesor).one()
    grupo = Tbl_grupo.query.filter(Tbl_grupo.id == id_grupo).one()
    curso_profesor = tbl_curso_profesor(curso, profesor, grupo)

    try:
        db.session.add(curso_profesor)
        db.session.commit()
        return 201
    except exc.OperationalError:
        db.session.rollback()
        return 403



def update_curso_profesor(curso_profesor_id, data):
    curso_profesor = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == curso_profesor_id).one()
    id_curso = data.get('id_curso')
    id_profesor = data.get('id_profesor')
    id_grupo = data.get('id_grupo')
    curso_profesor.curso = tbl_curso.query.filter(tbl_curso.id == id_curso).one()
    curso_profesor.profesor = tbl_usuario.query.filter(tbl_usuario.id == id_profesor).one() 
    curso_profesor.grupo = Tbl_grupo.query.filter(Tbl_grupo.id == id_grupo).one()
    
    try:
        db.session.add(curso_profesor)
        db.session.commit()
        return 204
    except  exc.OperationalError:
        db.session.rollback()
        return 403


def delete_curso_profesor(curso_profesor_id):
    curso_profesor = tbl_curso_profesor.query.filter(tbl_curso_profesor.id == curso_profesor_id).one()
    db.session.delete(curso_profesor)
    db.session.commit()



def create_canvas(data):# cambio de tabla, apuntar a curso_profesor
    contenido = data.get('contenido')
    id_usuario = data.get('id_usuario')
    estado = data.get('estado')
    usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()
    con = tbl_canvas(contenido, usuario, estado)
    db.session.add(con)
    db.session.commit()


def update_canvas(canvas_id, data):
    con = tbl_canvas.query.filter(tbl_canvas.id == canvas_id).one()
    con.contenido = data.get('contenido')
    con.estado= data.get('estado')
    id_usuario = data.get('id_usuario')
    con.usuario = tbl_usuario.query.filter(tbl_usuario.id == id_usuario).one()
    db.session.add(con)
    db.session.commit()


def delete_canvas(canvas_id):
    con = tbl_canvas.query.filter(tbl_canvas.id == canvas_id).one()
    db.session.delete(con)
    db.session.commit()


def create_asesoria(data):    
    id_estudiante = data.get('id_estudiante')
    encuestado = tbl_usuario.query.filter(tbl_usuario.id == id_estudiante).one()
    id_asesor = data.get('id_asesor')
    encuestador = tbl_usuario.query.filter(tbl_usuario.id == id_asesor).one()
    con = tbl_asesorias(encuestado, encuestador)
    db.session.add(con)
    db.session.commit()


def update_asesoria(asesoria_id, data):
    asesoria = tbl_asesorias.query.filter(tbl_asesorias.id == asesoria_id).one()
    id_estudiante = data.get('id_estudiante')
    id_asesor = data.get('id_asesor')
    asesoria.estudiante = tbl_usuario.query.filter(tbl_usuario.id == id_estudiante).one()
    asesoria.asesor = tbl_usuario.query.filter(tbl_usuario.id == id_asesor).one()
    try:
        db.session.add(asesoria)
        db.session.commit()
        return 204
    except exc.OperationalError:
        db.session.rollback()
        return 403


def create_encuesta(data):        
    asesorias_id = data.get('asesorias_id')
    asesoria = tbl_asesorias.query.filter(tbl_asesorias.id == asesorias_id).one()
    codigo = data.get('codigo')
    evidencia = data.get('evidencia')
    validacion = data.get('validacion')
    estado_id = data.get('estado_id')
    estado = tbl_estado.query.filter(tbl_estado.id == estado_id).one()
    con = tbl_encuesta(codigo, asesoria, estado, evidencia, validacion)
    db.session.add(con)
    db.session.commit()
    encuesta = {}
    encuesta['id'] = con.id
    encuesta['id_asesoria'] = con.asesorias_id
    encuesta['id_estado'] = con.estado_id    
    return encuesta

def update_encuesta(encuesta_id, data):
    encuesta = tbl_encuesta.query.filter(tbl_encuesta.id == encuesta_id).one()
    asesorias_id = data.get('asesorias_id')
    encuesta.asesoria = tbl_asesorias.query.filter(tbl_asesorias.id == asesorias_id).one()
    encuesta.codigo = data.get('codigo')
    encuesta.evidencia = data.get('evidencia')
    encuesta.validacion = data.get('validacion')
    estado_id = data.get('estado_id')
    encuesta.observacion = data.get('observacion')
    encuesta.estado = tbl_estado.query.filter(tbl_estado.id == estado_id).one()
    db.session.add(encuesta)
    db.session.commit()

# Validando encuesta AUDITOR
def delete_encuesta(id_encuesta):
    encuesta = tbl_encuesta.query.filter(tbl_encuesta.id == id_encuesta).one()
    encuesta.validacion = 1
    db.session.add(encuesta)
    db.session.commit()

def create_pregunta(data):
    pregunta = data.get('pregunta')
    categoria_id = data.get('categoria_id')
    categoria = tbl_categoria.query.filter(tbl_categoria.id == categoria_id)
    con = tbl_preguntas(pregunta, categoria)
    db.session.add(con)
    db.session.commit()



def update_pregunta(pregunta_id, data):
    pregunta = tbl_preguntas.query.filter(tbl_preguntas.id == pregunta_id).one()
    categoria_id = data.get('categoria_id')
    pregunta.categoria_id = tbl_categoria.query.filter(tbl_categoria.id == categoria_id).one()
    pregunta.pregunta = data.get('pregunta')    
    db.session.add(pregunta)
    db.session.commit()



def create_respuesta(data):        
    pregunta_id = data.get('pregunta_id')
    pregunta = tbl_preguntas.query.filter(tbl_preguntas.id == pregunta_id).one()
    encuesta_id = data.get('encuesta_id')
    encuesta = tbl_encuesta.query.filter(tbl_encuesta.id == encuesta_id).one()
    respuesta = data.get('respuesta')
    observaciones = data.get('observaciones')
    calificacion_id = data.get('calificacion_id')
    calificacion = tbl_calificacion.query.filter(tbl_calificacion.id == calificacion_id).one()
    con = tbl_respuestas(pregunta, encuesta, respuesta, observaciones, calificacion)
    db.session.add(con)
    db.session.commit()


def update_respuesta(respuesta_id, data):
    respuesta = tbl_respuestas.query.filter(tbl_respuestas.id == respuesta_id).one()
    pregunta_id = data.get('pregunta_id')
    respuesta.pregunta = tbl_preguntas.query.filter(tbl_preguntas.id == pregunta_id).one()
    encuesta_id = data.get('encuesta_id')
    respuesta.encuesta = tbl_encuesta.query.filter(tbl_encuesta.id == encuesta_id).one()
    respuesta.respuesta = data.get('respuesta')
    respuesta.observaciones = data.get('observaciones')
    calificacion_id = data.get('calificacion_id')
    respuesta.calificacion = tbl_calificacion.query.filter(tbl_calificacion.id == calificacion_id).one()
    db.session.add(respuesta)
    db.session.commit()
