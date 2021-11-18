from . import Test
from flask import url_for
from EnGo.models.receipt import Receipt


class ReceiptTest(Test):

    def setUp(self):
        Test.setUp(self)
        self.receipt = Receipt(
            customer_id=1
        )
        self.receipt.add()


class TestGetReceipts(ReceiptTest):

    def test_should_return_list_of_all_receipts_given_get_request(self):
        response = self.client.get(
            url_for('receipts')
        )
        
        self.assertEqual(len(response.json), 1)


class TestGetReceipt(ReceiptTest):

    def test_should_retrive_receipt_given_get_request_and_valid_receipt_id(self):
        response = self.client.get(
            url_for('receipts', receipt_id=self.receipt.id)
        )
        
        self.assertEqual(response.json['id'], self.receipt.id)


class TestAddReceipt(ReceiptTest):
    
    def test_should_add_receipt_given_post_request_with_valid_receipt_data(self):
        data = dict(
            customer_id=self.receipt.id
        )
        self.client.post(
            url_for('receipts'),
            json=data
        )

        self.assertEqual(len(Receipt.query.all()), 2)


class TestDeleteReceipt(ReceiptTest):

    def test_should_delete_receipt_given_valid_receipt_id(self):
        self.client.delete(
            url_for('receipts', receipt_id=self.receipt.id)
        )

        self.assertNotIn(self.receipt, self.db.session)
