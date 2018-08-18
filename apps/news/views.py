# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse

from django.contrib import messages

# Create your views here.

def show(request):
    return render('news/show.html')
