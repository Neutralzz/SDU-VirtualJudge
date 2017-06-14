"""SDUVJ URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from vj import views

handler404 = 'OJ.views.page_not_found'

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', views.login),
    url(r'^accounts/login/$',views.login),
    url(r'^register/$', views.register),
    url(r'^logout/$', views.logout),
    url(r'^problem/$', views.problem),
    url(r'^problem/([0-9]+)/$', views.problem_detail),
    url(r'^problem/([0-9]+)/submit/$', views.problem_submit),
    url(r'^problem/([0-9]+)/discuss/$', views.problem_discuss),
    url(r'^status/$', views.status),
    url(r'^show_source/$', views.show_source),
    
    url(r'^admin/', admin.site.urls),
    url(r'^profile/$', views.profile),

    url(r'^contest/$', views.contest),
    url(r'^contest/addcontest/$', views.contest_add),
    url(r'^contest/addcontest/get_problem_title/$',views.addcontest_get_problem_title),
    url(r'^contest/addcontest/submit/$', views.contest_add_process),
    

    url(r'^contest/([0-9]+)/$', views.contest_detail),
    url(r'^contest/([0-9]+)/modify/$', views.contest_modify),
    url(r'^contest/([0-9]+)/modify/submit/$', views.contest_modify_process),
    
    url(r'^contest/([0-9]+)/get_problem$', views.contest_get_problem),
    url(r'^contest/([0-9]+)/status/$', views.contest_status),
    url(r'^contest/([0-9]+)/submit/$', views.contest_submit),
    url(r'^contest/([0-9]+)/time/$', views.contest_time),
    url(r'^contest/([0-9]+)/rank/$', views.contest_rank),
    url(r'^rank/$', views.rank),
    url(r'^about/$', views.about),
]
