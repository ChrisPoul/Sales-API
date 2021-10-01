from flask import request
from flask_restful import Resource, marshal_with, fields
from .models.receipt import Receipt, SoldProduct

product_fields = dict(
    name=fields.String,
    price=fields.Integer
)

receipt_fields = dict(
    id=fields.Integer,
    customer_id=fields.Integer,
    sold_products=fields.List(fields.Nested(product_fields))
)


class ReceiptResource(Resource):

    @marshal_with(receipt_fields)
    def get(self, receipt_id=None):
        if receipt_id is None:
            return Receipt.query.all()
        
        return Receipt.query.get(receipt_id)

    def post(self):
        receipt = Receipt(
            customer_id=request.form['customer_id']
        )
        receipt.add()

    def put(self, receipt_id):
        receipt = Receipt.query.get(receipt_id)
        receipt.update()

    def delete(self, receipt_id):
        receipt = Receipt.query.get(receipt_id)
        receipt.delete()


sold_product_fields = dict(
    id=fields.Integer,
    receipt_id=fields.Integer,
    product_id=fields.Integer,
    quantity=fields.Integer
)


class SoldProductResource(Resource):

    @marshal_with(sold_product_fields)
    def get(self, sold_product_id=None):
        if sold_product_id is None:
            return SoldProduct.query.all()
        
        return SoldProduct.query.get(sold_product_id)

    def post(self):    
        sold_product = SoldProduct(
            receipt_id=request.form['receipt_id'],
            product_id=request.form['product_id'],
            quantity=request.form['quantity']
        )
        sold_product.add()

    def put(self, sold_product_id: int):
        sold_product = SoldProduct.query.get(sold_product_id)
        sold_product.update(request.form)

    def delete(self, sold_product_id):
        sold_product = SoldProduct.query.get(sold_product_id)
        sold_product.delete()

