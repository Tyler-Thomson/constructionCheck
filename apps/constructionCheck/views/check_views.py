from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..models import User

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def getCurrentUser(request):
    user_id = request.session['user_id']
    current_user = User.objects.get(id=user_id)
    return current_user

def getChecks(request):
    pass

def createCheck(request):
    pass

def showCheck(request):
    pass

def updateCheck(request):
    pass

def destroyCheck(request):
    pass
