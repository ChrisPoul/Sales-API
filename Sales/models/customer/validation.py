class CustomerValidation:

    def __init__(self, customer):
        self.customer = customer
        self.error = None

    def validate_name(self):
        customer_name = self.customer.name.replace(" ", "")
        if customer_name.isalpha() is False:
            self.error = "El nombre solo puede contener letras"
        return self.error
