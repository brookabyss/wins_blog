from django.conf.urls import url
from . import views
from django.conf import settings


app_name="main"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
]
