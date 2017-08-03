# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Attendee(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    club = models.CharField(max_length = 7)

class AttendedDate(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    date = models.DateField()
