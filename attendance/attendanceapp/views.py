# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

import datetime

from attendanceapp.forms import LoginForm
from attendanceapp.models import Attendee
from django.views.generic.edit import CreateView

# Create your views here.


def hello(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html")

def login(request):
   username = "not logged in"

   if request.method == "POST":
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()

   return render(request, 'loggedin.html', {"username" : username})

class AttendeeCreate(CreateView):
   model = Attendee
   fields = ['first_name', 'last_name', 'club']
