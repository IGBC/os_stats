"""osstats URL Configuration

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

from django.contrib.auth import views as auth_views
from core import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Root view "/"
    url(r'^$', views.index, name='index'),

    # Detail view for users and machines
    url(r'^user/(?P<user_id>[0-9]+)/$', views.detail_user, name='detail_user'),
    url(r'^rig/(?P<install_id>[0-9]+)/$', views.detail_machine, name='detail_machine'),

    # List of users and machines
    url(r'^users/$', views.list_users, name='list_users'),
    url(r'^rigs/$', views.list_machines, name='list_rigs'),

    # Login, authentication and registration
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

    # url(r'^stats/$', views.list_machines, name='list_rigs'),
    # url(r'^join/$', views.list_machines, name='list_rigs'),
]
