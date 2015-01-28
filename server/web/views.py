from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web.models import Bill
from web.serializers import BillSerializer

@api_view(['GET', 'POST'])
def bill_list(request, format=None):
    """
    List all code web, or create a new bill.
    """
    if request.method == 'GET':
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bill_detail(request, pk, format=None):
    """
    Retrieve, update or delete a bill.
    """
    try:
        bill = Bill.objects.get(pk=pk)
    except Bill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillSerializer(bill)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(bill, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
