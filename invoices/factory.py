import factory
from factory.django import DjangoModelFactory
from invoices.models import Invoice, InvoiceDetail
from faker import Factory

faker = Factory.create()

class InvoiceFactory(DjangoModelFactory):
    class Meta:
        model = Invoice

    invoice_no = faker.pyint()
    customer_name = faker.name()
    date = faker.date()

class InvoiceDetailFactory(DjangoModelFactory):
    class Meta:
        model = InvoiceDetail

    invoice = factory.SubFactory(InvoiceFactory)
    description = faker.text()
    quantity = faker.pydecimal(left_digits=11, right_digits=4, positive=True)
    unit = faker.random_element(elements=('kg', 'g',))
    price = faker.pydecimal(left_digits=11, right_digits=4, positive=True)

