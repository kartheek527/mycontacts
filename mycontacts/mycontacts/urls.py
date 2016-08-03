"""mycontacts URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from connection import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="login.html")),
    url(r'^accounts/profile/$', views.home),
    url(r'^logout/$', logout, {'template_name': 'index.html', 'next_page': '/'}, name='log_out'),
]
