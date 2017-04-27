# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Attendee(models.Model):
    GROUP_NAMES = (
        ('cubbies', 'Cubbies'),
        ('sparks', 'Sparks'),
        ('tnt', 'TNT'),
        ('trek', 'Trek'),
        ('journey', 'Journey'),
    )
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    group = models.CharField(max_length = 7, choices=GROUP_NAMES)

    def __str__(self):
        return self.first_name + " " + self.last_name
