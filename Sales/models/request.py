class SalesRequest:

    def __init__(self, sales_object):
        self.sales_object = sales_object

    def add(self):
        error = self.sales_object.validation.validate()
        if error is None:
            self.sales_object.add()

        return error

    def update(self, **kwargs):
        self.sales_object.update(**kwargs)
        error = self.sales_object.validation.validate()
        if error is None:
            self.sales_object.save()

        return error
