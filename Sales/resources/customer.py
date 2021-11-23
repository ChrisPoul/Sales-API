from flask import request
from flask_restful import (
    Resource, marshal_with, fields
)
from Sales.models.customer import Customer
from .receipt import receipt_fields


customer_fields = dict(
    id=fields.Integer,
    name=fields.String,
    phone=fields.String,
    receipts=fields.List(
        fields.Nested(receipt_fields)
    )
)


class CustomerResource(Resource):

    @marshal_with(customer_fields)
    def get(self, customer_id=None):
        if customer_id:
            return Customer.query.get(customer_id)

        return Customer.query.all()

    def post(self):
        form = request.get_json()
        customer = Customer(**form)
        customer.add()

    def put(self, customer_id):
        customer = Customer.query.get(customer_id)
        customer.update(request.get_json())