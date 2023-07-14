from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from invoices.models import Invoice
from invoices.serializer import InvoiceSerializer


# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [AllowAny]
