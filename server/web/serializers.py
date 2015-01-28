from django.forms import widgets
from rest_framework import serializers
from web.models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'amount', 'description')

