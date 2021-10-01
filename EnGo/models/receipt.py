from requests import get
from sqlalchemy import (
    Column, Integer, DateTime
)
from sqlalchemy.sql import func
from . import db, Model


class Receipt(db.Model, Model):
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())
    sold_products = db.relationship(
        'SoldProduct',
        backref='receipt',
        cascade='all, delete-orphan'
    )


class SoldProduct(db.Model, Model):
    id = Column(Integer, primary_key=True)
    receipt_id = Column(Integer, db.ForeignKey('receipt.id'), nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())

    @property
    def product(self):
        return get(f'http://127.0.0.1:5000/inventory/products/{self.product_id}').json()
