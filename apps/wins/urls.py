from django.conf.urls import url
from . import views
from django.conf import settings


app_name="wins"
urlpatterns = [
    url(r'^all$', views.show, name='show'),

]
