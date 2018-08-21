# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from ..personnel.models import Personnel
from ..news.models import News
from ..wins.models import Wins
from ..personnel.personnel_serializer import PersonnelSerializer
from ..personnel.json_encoder import JSONEncoder


import json

status=""

def index(request):
    print("index")
    all_personnel = Personnel.objects.all()
    serializedPersonnel = PersonnelSerializer(all_personnel, many = True)

    context ={
    "news": News.objects.order_by('created_at')[:3],
    "wins": Wins.objects.order_by('created_at')[:3],
    "personnel":json.dumps(serializedPersonnel.data)
    }
    return render(request,"main/index.html",context)
