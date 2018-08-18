# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Personnel (models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    fun_fact = models.CharField(max_length=255, blank=True)
    profile_image = models.FileField (upload_to = 'profile_images/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class PersonnelForm (forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ('first_name','last_name', 'fun_fact', 'profile_image')
