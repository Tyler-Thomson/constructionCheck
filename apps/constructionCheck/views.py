from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def getCurrentUser(request):
    user_id = request.session['user_id']
    current_user = User.objects.get(id=user_id)
    return current_user

def index(request):
    print "Inside the index method"
    return render(request, 'constructionCheck/index.html')

def create(request):
    print "Inside the create method"

    if request.method == 'POST':     #Validates that only POST data is received
        form_data = request.POST
        check = User.objects.validate_reg(form_data)     #Stores the validate function from models, contains error list
        if check != []:     #If there are errors, redirect to homepage
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

def success(request):
    print "Inside the success method"
    if 'user_id' in request.session:
        user_id = request.session['user_id'] #store the user id from sessions in a variable
        current_user = User.objects.get(id=user_id)

        context = {
            'name': current_user.first_name
        }
        return render(request, 'login_and_registration_app/success.html', context)
    return redirect('/')

def login(request):
    print "Inside the login method"
    if request.method == "POST":
        form_data = request.POST
        check = User.objects.authenticate(form_data)

        if type(check) == type(User()):
            return redirect('/success')
        print check #You need to make sure the login makes it to the success page
    return redirect('/')


def logout(request):
    request.session.pop('user_id')
    return redirect('/')
