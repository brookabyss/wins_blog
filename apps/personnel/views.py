# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse

from django.contrib import messages

from .models import PersonnelForm,Personnel

# Create your views here.
def new(request):
    form = PersonnelForm()
    return render(request,'personnel/new.html',{'form':form})

def create(request):
    print("create personnel")
    if request.method == 'POST':
        print ("hello")
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'personnel/show.html')
        else:
            form = PersonnelForm()
    return render(request,'personnel/new.html',{'form':form})

def show(request):
    context = {
        "personnel": Personnel.objects.all()
    }
    return render(request,'personnel/show.html',context)
