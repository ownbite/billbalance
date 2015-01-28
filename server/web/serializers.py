from django.forms import widgets
from rest_framework import serializers
from web.models import Bill
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    bills = serializers.PrimaryKeyRelatedField(many=True, queryset=Bill.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bills')

class BillSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bill
        fields = ('id', 'amount', 'description', 'owner')

