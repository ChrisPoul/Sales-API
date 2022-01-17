from . import CustomerTest


class TestValidateName(CustomerTest):

    def test_should_not_return_error_given_valid_name(self):
        self.customer.name = "Valid Name"
        error = self.customer.validation.validate_name()

        self.assertEqual(error, None)
