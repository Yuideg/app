from rest_framework import serializers
from invoices.models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all(), allow_null=True, required=False)

    class Meta:
        model = InvoiceDetail
        fields = ('id', 'invoice', 'description', 'quantity', 'unit', 'price')


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('id', 'invoice_no', 'customer_name', 'date', "details")

    def create(self, validated_data):
        details = validated_data.pop("details")
        invoice_obj = Invoice.objects.create(**validated_data)
        for invoice_detail in details:
            InvoiceDetail.objects.create(**invoice_detail, invoice=invoice_obj)
        return invoice_obj
