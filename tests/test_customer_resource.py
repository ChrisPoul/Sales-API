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


class TestUpdateCustomer(CustomerTest):

    def test_should_update_customer_given_put_request_and_valid_customer_id_and_customer_data(self):
        customer_data = dict(
            name="New Name",
            phone="New Phone"
        )
        self.client.put(
            url_for("customers", customer_id=self.customer.id),
            json=customer_data
        )

        self.assertEqual(self.customer.name, "New Name")


class TestDeleteCustomer(CustomerTest):

    def test_should_delete_customer_given_delete_request_and_valid_customer_id(self):
        self.client.delete(
            url_for("customers", customer_id=self.customer.id)
        )

        self.assertNotIn(self.customer, self.db.session)
