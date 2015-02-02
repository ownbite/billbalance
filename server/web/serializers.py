from rest_framework import serializers
from web.models import Bill, Node
from django.contrib.auth.models import User


class BillSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bill
        fields = ('url', 'amount', 'description', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    bills = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='bill-detail',
                                                queryset=Bill.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'bills')

class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Node
        fields = ('url', 'parentNode', 'name', 'description', 'subnodes')

