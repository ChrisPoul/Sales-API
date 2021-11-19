from sqlalchemy import (
    Column, Integer, DateTime
)
from sqlalchemy.sql import func
from . import db, Model


class Customer(db.Model, Model):
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())
    receipts = db.relationship(
        'Receipt',
        backref="customer",
        cascade="all, delete-orphan"
    )
