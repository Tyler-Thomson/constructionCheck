from rest_framework import permissions, viewsets
from __future__ import unicode_literals
from ..serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
