# backendSiempre

Backend del sistema Siempre

# Pasos para la instalacion

*/Instalar Envorno Virtual*/

sudo apt install virtualenv

virtualenv -p python3 env


source env/bin/activate

sudo apt-get install libmysqlclient-dev

pip install -r requirements.txt

python setup.py develop



pip install --upgrade Werkzeug==0.16.0

*/Correr programa*/

python rest_api_demo/app.py

*/Poner en Requeriments*/

aniso8601==8.0.0
attrs==19.3.0
click==7.1.2
Flask==1.1.2
flask-restplus==0.9.2
Flask-SQLAlchemy==2.1
importlib-metadata==1.7.0
itsdangerous==1.1.0
Jinja2==2.11.2
jsonschema==3.2.0
MarkupSafe==1.1.1
pyrsistent==0.16.0
pytz==2020.1
-e git+https://github.com/postrational/rest_api_demo.git@1660892257a41e19f8c7b21c81fbb05be5c188d5#egg=rest_api_demo
six==1.15.0
SQLAlchemy==1.3.18
Werkzeug==0.16.0
zipp==3.1.0
python setup.py develop
pip install --upgrade Werkzeug==0.16.0
python rest_api_demo/app.py
MILTON ALEXANDER LONDOÑO ROMÁN11:07
aniso8601==8.0.0
attrs==19.3.0
click==7.1.2
Flask==1.1.2
flask-restplus==0.9.2
Flask-SQLAlchemy==2.1
importlib-metadata==1.7.0
itsdangerous==1.1.0
Jinja2==2.11.2
jsonschema==3.2.0
MarkupSafe==1.1.1
pyrsistent==0.16.0
pytz==2020.1
six==1.15.0
SQLAlchemy==1.3.18
Werkzeug==0.16.0
zipp==3.1.0
MILTON ALEXANDER LONDOÑO ROMÁN11:12
pip freeze > requiriments.txt
MILTON ALEXANDER LONDOÑO ROMÁN11:20
aniso8601==8.0.0
attrs==19.3.0
click==7.1.2
Flask==1.1.2
flask-restplus==0.9.2
Flask-SQLAlchemy==2.1
importlib-metadata==1.7.0
itsdangerous==1.1.0
Jinja2==2.11.2
jsonschema==3.2.0
MarkupSafe==1.1.1
pyrsistent==0.16.0
pytz==2020.1
six==1.15.0
SQLAlchemy==1.3.18
Werkzeug==0.16.0
zipp==3.1.0
