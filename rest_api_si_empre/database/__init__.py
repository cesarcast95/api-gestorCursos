from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from rest_api_si_empre.database.models import tbl_roles  # noqa
    db.drop_all()
    db.create_all()
