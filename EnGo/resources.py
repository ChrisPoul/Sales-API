from flask import request
from flask_restful import Resource, marshal_with, fields
from .models.receipt import Receipt
from .models.sold_product import SoldProduct

sold_product_fields = dict(
    id=fields.Integer,
    receipt_id=fields.Integer,
    product_id=fields.Integer,
    quantity=fields.Integer,
    price=fields.Float,
    total=fields.Float
)

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


class SoldProductResource(Resource):

    @marshal_with(sold_product_fields)
    def get(self, sold_product_id=None):
        if sold_product_id is None:
            return SoldProduct.query.all()
        
        return SoldProduct.query.get(sold_product_id)

    def post(self):
        form = request.get_json()
        sold_product = SoldProduct(
            receipt_id=form['receipt_id'],
            product_id=form['product_id'],
            quantity=form['quantity'],
            price=form['price']
        )
        sold_product.add()

    def put(self, sold_product_id: int):
        sold_product = SoldProduct.query.get(sold_product_id)
        sold_product.update(request.get_json())

    def delete(self, sold_product_id):
        sold_product = SoldProduct.query.get(sold_product_id)
        sold_product.delete()

