# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from attendanceapp.models import Attendee
from attendanceapp.models import AttendedDate

# Register your models here.

admin.site.register(Attendee)
admin.site.register(AttendedDate)
