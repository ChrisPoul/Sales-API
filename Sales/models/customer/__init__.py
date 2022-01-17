from sqlalchemy import (
    Column, Integer, DateTime,
    String
)
from sqlalchemy.sql import func
from . import db, Model


class Customer(db.Model, Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False, unique=False)
    phone = Column(String(17), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=False, default="")
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())
    receipts = db.relationship(
        'Receipt',
        backref="customer",
        cascade="all, delete-orphan"
    )
