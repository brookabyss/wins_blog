from django.conf.urls import url
from . import views
from django.conf import settings

from django.conf.urls.static import static

from django.views.static import serve



app_name="personnel"
urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^show$', views.show, name='show'),
    url(r'^show/(?P<user_id>\d+)$', views.view, name='view'),



]

# make sure to change media serve for production use a front end server for media files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
