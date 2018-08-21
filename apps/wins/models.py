# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.


class Wins (models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class WinsForm (forms.ModelForm):
    description = forms.CharField( widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Wins
        fields = ('title','description')
