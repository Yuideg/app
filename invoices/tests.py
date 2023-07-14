from rest_framework.test import APITestCase
from invoices.factory import InvoiceDetailFactory, InvoiceFactory


# Create your tests here.
class InvoiceTestCase(APITestCase):
    def setUp(self):
        self.invoice = InvoiceFactory()
        self.invoice_detail = InvoiceDetailFactory.create(invoice=self.invoice)


    def test_create_invoice(self):
        """
        Ensure that we can create invoice object.
        :return: invoice object
        """
        data = {
            "invoice_no": 730,
            "customer_name": "Yideg Misganaw",
            "details": [
                {
                    "description": "This is invoice description ",
                    "quantity": 10,
                    "unit": "g",
                    "price": 1200
                }
            ]

        }
        # TestCase 01: Use Valid data,then should create an invoice object(No validation error).
        response = self.client.post("/api/invoices/", data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["invoice_no"], data["invoice_no"])
        self.assertEqual(response.data["customer_name"], data["customer_name"])
        self.assertEqual(len(response.data["details"]), len(data['details']))

        # TestCase 02: Use InValid data,then should return an error message(validation error).
        data["invoice_no"]="invoice no"
        response = self.client.post("/api/invoices/", data, format='json')
        self.assertEqual(response.status_code, 400)



    def test_retrieve_invoice(self):
        """
        Ensure that we can retrieve(GET) invoice object.
        :return: invoice object
        """
        # TestCase 01: Use Valid invoice id params in the request url(existing invoice id).
        response = self.client.get("/api/invoices/{}/".format(self.invoice.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["invoice_no"], self.invoice.invoice_no)
        self.assertEqual(response.data["customer_name"], self.invoice.customer_name)
        self.assertEqual(len(response.data["details"]), 1)

        # TestCase 01: Use InValid invoice id params in the request url(non-existing invoice id).
        response = self.client.get("/api/invoices/{}/".format(self.invoice.id+10))
        self.assertEqual(response.status_code, 404)

    def test_list_invoice(self):
        """
        Ensure that we can retrieve(GET) invoice object.
        :return: invoice object
        """
        # TestCase 01: Use Valid url,then should return list of created instance of invoices(db).
        response = self.client.get("/api/invoices/")
        self.assertEqual(response.status_code, 200)
