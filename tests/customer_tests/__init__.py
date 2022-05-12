from tests import Test
from Sales.models.customer import Customer


class CustomerTest(Test):

    def setUp(self):
        Test.setUp(self)
        self.customer = Customer(
            name="Test Name",
            phone="Test Phone"
        )
        self.customer.add()
