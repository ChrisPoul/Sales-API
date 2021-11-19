from flask import request
from flask_restful import (
    Resource, marshal_with, fields
)
from EnGo.models.receipt import Receipt
from .sold_product import sold_product_fields

receipt_fields = dict(
    id=fields.Integer,
    customer_id=fields.Integer,
    sold_products=fields.List(fields.Nested(sold_product_fields))
)


class ReceiptResource(Resource):

    @marshal_with(receipt_fields)
    def get(self, receipt_id=None):
        if receipt_id is None:
            return Receipt.query.all()

        return Receipt.query.get(receipt_id)

    def post(self):
        form = request.get_json()
        receipt = Receipt(
            customer_id=form['customer_id']
        )
        receipt.add()

    def put(self, receipt_id):
        receipt = Receipt.query.get(receipt_id)
        receipt.update()

    def delete(self, receipt_id):
        receipt = Receipt.query.get(receipt_id)
        receipt.delete()