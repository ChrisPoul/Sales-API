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
