"""djangoSPD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.main.urls',namespace='main' , app_name='main')),
    url(r'^personnel/', include('apps.personnel.urls',namespace='personnel' , app_name='personnel')),
    url(r'^news/', include('apps.news.urls',namespace='news' , app_name='news')),
    url(r'^wins/', include('apps.wins.urls',namespace='wins' , app_name='wins')),



]
