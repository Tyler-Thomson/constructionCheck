from models import State, Checklist, Section, Check
from rest_framework import serializers

from django.contrib.auth import get_user_model #Required b/c custom User model
User = get_user_model()#Required b/c custom User model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    checklists = serializers.HyperlinkedRelatedField(read_only=True, view_name='checklist-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'checklists', 'email', 'password',
                                        'is_active', 'is_admin', 'created_at', 'updated_at')

class StateSerializer(serializers.HyperlinkedModelSerializer):
    houses = serializers.HyperlinkedRelatedField(queryset=Checklist.objects.all(), view_name='checklist-detail', many=True)

    class Meta:
        model = State
        fields = ('url', 'id', 'state', 'houses')

class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    manager = UserSerializer
    checks = serializers.StringRelatedField(many=True)
    # checks = HyperlinkedRelatedField(queryset=Check.objects.all(), view_name='check-detail', many=True)
    class Meta:
        model = Checklist
        fields = ('url', 'id', 'address', 'city', 'zipcode', 'state', 'checks', 'manager')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    checks = serializers.HyperlinkedRelatedField(read_only=True, view_name='check-detail', many=True)

    class Meta:
        model = Section
        fields = ('url', 'id', 'name', 'checks')

class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Check
        fields = ('url', 'id', 'check', 'section', 'checklist')
