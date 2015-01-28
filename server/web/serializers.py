from django.forms import widgets
from rest_framework import serializers
from web.models import Bill


# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)

# class PersonSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'amount', 'description')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Bill` instance, given the validated data.
    #     """
    #     return Bill.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Bill` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
