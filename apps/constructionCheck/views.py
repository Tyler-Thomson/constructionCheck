from __future__ import unicode_literals
from rest_framework import permissions, viewsets
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HouseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows houses to be viewed or edited
    """
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class ChecklistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checklists to be viewed or edited
    """
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sections to be viewed or edited
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class CheckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
