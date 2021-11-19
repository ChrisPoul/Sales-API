from flask import request
from flask_restful import Resource, marshal_with, fields
from EnGo.models.sold_product import SoldProduct

sold_product_fields = dict(
    id=fields.Integer,
    receipt_id=fields.Integer,
    product_id=fields.Integer,
    quantity=fields.Integer,
    price=fields.Float,
    total=fields.Float
)


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
