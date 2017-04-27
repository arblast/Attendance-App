# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Attendee(models.Model):
    GROUP_NAMES = (
        ('C', 'Cubbies'),
        ('S', 'Sparks'),
        ('T', 'TNT'),
        ('Tr', 'Trek'),
        ('J', 'Journey'),
    )
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    group = models.CharField(max_length = 2, choices=GROUP_NAMES)

    def __str__(self):
        return self.first_name + " " + self.last_name
