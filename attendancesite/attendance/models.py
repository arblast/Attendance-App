# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models



class Attendee(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
