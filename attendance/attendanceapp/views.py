# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def hello(request):
    text= """<h1>Welcome to my app!</h1>"""
    return HttpResponse(text)

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticles(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)
