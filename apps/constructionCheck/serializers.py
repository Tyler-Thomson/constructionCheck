from django.contrib.auth.models import User
from models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                                            'created_at', 'updated_at')

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'address', 'city', 'user', 'checklist',
                                    'created_at', 'updated_at')

class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checklist
        fields = ('id', 'house', 'checks', 'created_at', 'updated_at')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'checks', 'created_at', 'updated_at')

class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Check
        fields = ('id', 'section', 'checklist', 'created_at', 'updated_at')