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
from django.views.generic import TemplateView, ListView
from connection import views, models
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='login.html')),
    url(r'^auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout, {'template_name': 'index.html', 'next_page': '/'},
        name='log_out'),
    # Below urls for CRUD operation.
    url(r'^accounts/profile/$', views.home, name = 'contact_list'),
    url(r'^save_contact/$', views.save_contact, name = 'new_contact'),
    url(r'^update_contact/(?P<pk>\d+)$', views.update_contact, name='update_contact'),
    url(r'^delete_contact/(?P<pk>\d+)$', views.delete_contact, name='delete_contact'),

    # Using generic Listview in url itself
    #
    # url(r'^accounts/profile/$', ListView.as_view(
    #                 model=models.Contact,
    #                 queryset=models.Contact.objects.filter(admin = request.user),
    #                 context_object_name="contacts",
    #                 template_name='home.html'), name="contact_list"),
]
