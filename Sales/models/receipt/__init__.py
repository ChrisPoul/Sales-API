from sqlalchemy import (
    Column, Integer, DateTime
)
from sqlalchemy.sql import func
from Sales.models import db, Model


class Receipt(db.Model, Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=False, nullable=False)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())
    sold_products = db.relationship(
        'SoldProduct',
        backref='receipt',
        cascade='all, delete-orphan'
    )

    @property
    def validation(self):
        from .validation import ReceiptValidation
        return ReceiptValidation(self)
