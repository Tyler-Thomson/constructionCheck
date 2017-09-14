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

def getHouses(request):
    pass

def createHouse(request):
    pass

def showHouse(request):
    pass

def updateHouse(request):
    pass

def destroyHouse(request):
    pass
