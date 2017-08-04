# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import JsonResponse

import datetime
import pdb

from attendanceapp.forms import LoginForm
from attendanceapp.models import Attendee
from attendanceapp.models import AttendedDate
from django.views import View

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

class AttendeeView(View):

    def get(self, request):
        attendees = Attendee.objects.all()
        first_names = []
        for attendee in attendees:
            first_names.append(attendee.first_name)
        props = {
            'attendees': first_names
        }
        return JsonResponse(props)

    def post(self, request):
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        club = data.get("club")
        new_attendee = Attendee(first_name = first_name, last_name = last_name,
        club = club)
        new_attendee.save()
        props = { 'attendee': new_attendee.first_name}
        return JsonResponse(props)

class DateView(View):

    def get(self, request):
        data = request.GET.get("date")
        year = data.year
        month = data.month
        day = data.day
        date = datetime.date(year, month, day)
        attended_dates = AttendedDates.objects.filter(date=date)
        props = { 'dates': attended_dates}
        return JsonResponse(props)

    def post(self, request):
        data = request.POST
        date = data.get("date")
        attendee_id = data.get("attendee_id")
        attendee = Attendee.objects.filter(id = attendee_id)
        attended_date = AttendedDate(date = date, attendee = attendee)
        attended_date.save()
        props = { 'attendee': attendee }
        return JsonResponse(props)
