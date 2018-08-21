# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse

from django.contrib import messages

from .models import News, NewsForm

# Create your views here.


def new(request):
    form = NewsForm()
    return render(request,'news/new.html',{'form':form})

def create(request):
    print("create personnel")
    if request.method == 'POST':
        print ("hello")
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:show'))
        else:
            form = NewsForm()
    return render(request,'news/new.html',{'form':form})

def show(request):
    context = {
    "news": News.objects.all()
    }
    return render(request, 'news/show.html', context)

def newsDetail (request,news_id):

    context = {
        "news": News.objects.filter(id=news_id)[0]
    }
    return render(request,'news/display.html',context)
