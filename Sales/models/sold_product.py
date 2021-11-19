from sqlalchemy import (
    Column, Integer, DateTime
)
from sqlalchemy.sql import func
from . import db, Model


class SoldProduct(db.Model, Model):
    id = Column(Integer, primary_key=True)
    receipt_id = Column(Integer, db.ForeignKey('receipt.id'), nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    price = Column(Integer, nullable=False, default=0)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())

    @property
    def total(self):
        return self.quantity * self.price
