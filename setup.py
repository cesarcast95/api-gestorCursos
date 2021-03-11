from setuptools import setup, find_packages

setup(
    name='rest_api_si_empre',
    version='1.0.0',
    description='Boilerplate code for a RESTful API based on Flask-RESTPlus',
    url='https://github.com/postrational/rest_api_demo',
    author='Team si_empre',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='rest restful api flask swagger openapi flask-restplus',

    packages=find_packages(),

    install_requires=['flask-restplus==0.13.0', 'Flask-SQLAlchemy==2.4.4', 'Flask-MySQL==1.5.1', 'PyMySQL==0.10.0', 'mysqlclient', 'flask-marshmallow'],
)
