# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse

from django.contrib import messages

from .models import Wins, WinsForm

# Create your views here.


def new(request):
    form = WinsForm()
    return render(request,'wins/new.html',{'form':form})

def create(request):
    print("create personnel")
    if request.method == 'POST':
        print ("hello")
        form = WinsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('wins:show'))
        else:
            form = WinsForm()
    return render(request,'wins/new.html',{'form':form})

def show(request):
    context = {
    "wins": Wins.objects.all()
    }
    return render(request, 'wins/show.html', context)

def winDetail (request,win_id):

    context = {
        "win": Wins.objects.filter(id=win_id)[0]
    }
    return render(request,'wins/display.html',context)
