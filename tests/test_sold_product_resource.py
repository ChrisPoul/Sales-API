from . import Test
from flask import url_for
from EnGo.models.sold_product import SoldProduct


class SoldProductTest(Test):

    def setUp(self):
        super().setUp()
        self.sold_product = SoldProduct(
            receipt_id=1,
            product_id=1,
            quantity=0
        )
        self.sold_product.add()


class TestGetSoldProducts(SoldProductTest):

    def test_should_return_list_of_all_sold_products_given_get_request(self):
        response = self.client.get(
            url_for('sold_products')
        )
        
        self.assertEqual(len(response.json), 1)


class TestGetSoldProduct(SoldProductTest):

    def test_should_retrive_sold_product_given_get_request_and_valid_sold_product_id(self):
        response = self.client.get(
            url_for('sold_products', sold_product_id=self.sold_product.id)
        )
        
        self.assertEqual(response.json['receipt_id'], self.sold_product.receipt_id)


class TestAddSoldProduct(SoldProductTest):

    def test_should_add_sold_product_given_post_request_and_valid_sold_product_data(self):
        sold_product_data = dict(
            receipt_id=1,
            product_id=2,
            quantity=0,
            price=10
        )
        with self.client as client:
            client.post(
                url_for('sold_products'),
                json=sold_product_data
            )
        
        self.assertNotEqual(SoldProduct.query.filter_by(product_id=2).first(), None)


class TestUpdateSoldProduct(SoldProductTest):

    def test_should_update_sold_product_given_put_request_and_valid_sold_product_data(self):
        sold_product_data = dict(
            quantity=5
        )
        self.client.put(
            url_for('sold_products', sold_product_id=self.sold_product.id),
            data=sold_product_data
        )

        self.assertEqual(self.sold_product.quantity, 5)


class TestDeleteSoldProduct(SoldProductTest):

    def test_should_delete_sold_product_given_valid_receipt_id(self):
        self.client.delete(
            url_for('sold_products', sold_product_id=self.sold_product.id)
        )

        self.assertNotIn(self.sold_product, self.db.session)
