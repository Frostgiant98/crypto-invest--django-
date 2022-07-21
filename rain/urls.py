"""rain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns , static
from . import settings
from myapp import views as appviews

urlpatterns = [
    path('zeus/', admin.site.urls),
    path('', appviews.homepage, name="homepage"),
    url(r'^dashboard', appviews.dashboard, name="dashboard"),
    url(r'^newdash', appviews.newdash, name="newdash"),
    url(r'^edit_profile', appviews.profile_edit, name="profile_edit"),

    url(r'^upgrade', appviews.upgrade, name="upgrade"),
    url(r'^withdraw', appviews.withdraw, name="withdraw"),
    url(r'^depositsret', appviews.deposits2, name="deposits2"),

    url(r'^user_list', appviews.user_list, name="user_list"),

    url(r'^notifi', appviews.user_list, name="notofications"),
    url(r'^deposit_list', appviews.deposit_list, name="deposit_list"),
    url(r'^deposit', appviews.deposits, name="deposits"),

    url(r'^admin_user_delete/(?P<user_id>\d+)/', appviews.admin_user_delete, name="admin_delete_user"),
    url(r'^admin_user_edit/(?P<user_id>\d+)/', appviews.admin_user_edit, name="admin_edit_user"),
    url(r'^admin_delete_user/(?P<user_id>\d+)/', appviews.admin_user_delete, name="admin_delete_user"),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', appviews.SignUpView.as_view(), name="signup"),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)