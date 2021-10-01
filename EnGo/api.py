from flask_restful import Api

api = Api(prefix='/sales')

from .resources import ReceiptResource
api.add_resource(
    ReceiptResource, 
    '/receipts', 
    '/receipts/<int:receipt_id>', 
    endpoint='receipts'
)

from .resources import SoldProductResource
api.add_resource(
    SoldProductResource, 
    '/sold_products', 
    '/sold_products/<int:sold_product_id>',
    endpoint='sold_products'
)