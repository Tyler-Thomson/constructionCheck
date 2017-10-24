from django.contrib.auth import get_user_model #Required b/c custom User model
from models import *
from rest_framework import serializers

User = get_user_model()#Required b/c custom User model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('url', 'id', 'first_name', 'last_name', 'email', 'password',
        #                 'is_active', 'is_admin', 'created_at', 'updated_at')

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
        # fields = ('url', 'id', 'address', 'city', 'zipcode', 'state', 'user',
        #                             'checklist', 'created_at', 'updated_at')

class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'
        # fields = ('url', 'id', 'house', 'checks', 'created_at', 'updated_at')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        # fields = ('url', 'id', 'name', 'checks', 'created_at', 'updated_at')

class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Check
        fields = '__all__'
        # fields = ('url', 'id', 'section', 'checklist', 'created_at', 'updated_at')
