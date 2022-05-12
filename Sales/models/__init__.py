from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Model:

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        print(kwargs)
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
