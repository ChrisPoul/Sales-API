from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Model:

    def add(self):
        db.session.add(self)
        self.save()

    def update(self, **kwargs):
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])

    def save(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        self.save()

    @property
    def request(self):
        from .request import SalesRequest
        return SalesRequest(self)
