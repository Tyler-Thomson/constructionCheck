# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model #Required b/c custom User model

User = get_user_model() #Required b/c custom User model

# def login(request):
#     print "Inside the root method"
#
# def profile(request):
#     print "Inside the profile method"
#
# def logout(request):
#     print "Inside the logout method"
