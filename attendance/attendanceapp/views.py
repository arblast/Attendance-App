# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

import datetime


# Create your views here.


def hello(request):
    today = datetime.datetime.now().date()
    return redirect("https://www.djangoproject.com")

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return redirect("articles", year = "2045", month = "02")

def viewArticles(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)
