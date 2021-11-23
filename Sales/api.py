from flask_restful import Api
from .resources.receipt import ReceiptResource
from .resources.sold_product import SoldProductResource
from .resources.customer import CustomerResource

api = Api(prefix='/sales')

api.add_resource(
    ReceiptResource,
    '/receipts',
    '/receipts/<int:receipt_id>',
    endpoint='receipts'
)

api.add_resource(
    SoldProductResource,
    '/sold_products',
    '/sold_products/<int:sold_product_id>',
    endpoint='sold_products'
)

api.add_resource(
    CustomerResource,
    '/customer',
    '/customer/<int:customer_id>',
    endpoint='customers'
)
