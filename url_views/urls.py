"""url_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from url_app.views import my_view
from url_app.views import my_index_view
from url_app.views import my_hello_view
from url_app.views import my_balloon_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_view),
    url(r'^$', my_index_view),
    url(r'^hello/$', my_hello_view),
    url(r'^99/red/balloons/$', my_balloon_view)

]
