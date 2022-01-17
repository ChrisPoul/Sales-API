from . import CustomerTest


class TestValidateName(CustomerTest):

    def test_should_not_return_error_given_valid_name(self):
        self.customer.name = "Valid Name"
        error = self.customer.validation.validate_name()

        self.assertEqual(error, None)

    def test_should_return_error_given_non_alphabetical_characters_in_name(self):
        self.customer.name = "1nv@l1id n@m3"
        error = self.customer.validation.validate_name()

        self.assertNotEqual(error, None)

    def test_should_return_error_given_empty_name(self):
        self.customer.name = ""
        error = self.customer.validation.validate_name()

        self.assertNotEqual(error, None)
