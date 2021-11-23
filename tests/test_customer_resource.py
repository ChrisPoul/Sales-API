from flask import url_for
from . import Test
from Sales.models import Customer


class CustomerTest(Test):

    def setUp(self):
        Test.setUp(self)
        self.customer = Customer(
            name="Test Name",
            phone="Test Phone"
        )
        self.customer.add()


class TestGetCustomer(CustomerTest):

    def test_should_return_customer_given_get_request_valid_customer_id(self):
        response = self.client.get(
            url_for("customers", customer_id=self.customer.id)
        )
        customer = response.json

        self.assertEqual(customer["name"], self.customer.name)


class TestGetCustomers(CustomerTest):

    def test_should_return_list_of_customers_given_get_request(self):
        response = self.client.get(
            url_for("customers")
        )

        self.assertEqual(len(response.json), 1)


class TestAddCustomer(CustomerTest):

    def test_should_save_customer_given_post_request_with_valid_customer_data_in_json_format(self):
        customer_data = dict(
            name="New Customer",
            phone="New Phone"
        )
        self.client.post(
            url_for("customers"),
            json=customer_data
        )
        customers = Customer.query.all()

        self.assertEqual(len(customers), 2)
