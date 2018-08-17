# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse
from django.contrib import messages

status=""
def index(request):
    print("index")
    return render(request,"loginReg/index.html")
