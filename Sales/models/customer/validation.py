class CustomerValidation:

    def __init__(self, customer):
        self.customer = customer
        self.error = None

    def validate(self):
        self.validate_name()
        if self.error is None:
            self.validate_phone()

        return self.error

    def validate_name(self):
        customer_name = self.customer.name.replace(" ", "")
        if customer_name.isalpha() is False:
            self.error = "El nombre solo puede contener letras y espacios"
        return self.error

    def validate_phone(self):
        customer_phone = self.customer.phone.replace(" ", "")
        if customer_phone.isnumeric() is False:
            self.error = "El número de teléfono solo puede contener números y espacios"

        return self.error
