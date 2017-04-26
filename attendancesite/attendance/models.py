# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Attendee(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.first_name + " " + self.last_name
