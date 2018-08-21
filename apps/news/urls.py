from django.conf.urls import url
from . import views
from django.conf import settings


app_name="news"
urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^show$', views.show, name='show'),
    url(r'^detail/(?P<news_id>\d+)$', views.newsDetail, name='news_detail'),



]
