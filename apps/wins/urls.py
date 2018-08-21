from django.conf.urls import url
from . import views
from django.conf import settings


app_name="wins"
urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^show$', views.show, name='show'),
    url(r'^detail/(?P<win_id>\d+)$', views.winDetail, name='win_detail'),


]
