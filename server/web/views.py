
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web.models import Bill, Node
from web.serializers import BillSerializer, UserSerializer, NodeSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from web.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
