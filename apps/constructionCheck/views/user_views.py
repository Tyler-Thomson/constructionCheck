from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..models import User

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def getCurrentUser(request):
    current_user = User.objects.get(id= request.session['user_id'])
    return current_user

def index(request):
    print "Inside the index method"
    return render(request, 'constructionCheck/index.html')

def success(request):
    if 'user_id' in request.session:
        print "Inside the success method"
        current_user = getCurrentUser(request)

        context = {
            'first_name': current_user.first_name
        }
        return render(request, 'constructionCheck/success.html', context)
    return redirect('/')

def login(request):
    print "Inside the login method"
    if request.method == "POST":
        form_data = request.POST
        check = User.objects.authenticate(form_data)

        if type(check) == type(User()):
            return redirect('/success')
        print check
    return redirect('/')

def logout(request):
    request.session.pop('user_id')
    return redirect('/')

def getUsers(request):
    if 'user_id' in request.session:
        print "Inside the getUsers method"
        users = User.objects.all()

        context = {
            'users': users
        }
        return render(request, 'constructionCheck/getUsers.html', context)
    return redirect('/')

def createUser(request):
    print "Inside the create method"
    if request.method == 'POST':
        form_data = request.POST
        check = User.objects.validate_reg(form_data)
        if check != []:
            print check
            return redirect('/')
        else:
            user = User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = form_data['password']
            )
            request.session['user_id'] = user.id
            print user
            print check
    return redirect('/success')

def showUser(request, id):
    pass

def updateUser(request):
    pass
