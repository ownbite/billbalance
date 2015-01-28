from django.conf.urls import patterns, include, url
from django.contrib import admin

from web import views

urlpatterns = patterns('',
    url(r'^bill/$', views.bill_list),
    url(r'^bill/(?P<pk>[0-9]+)/$', views.bill_detail),

    url(r'^admin/', include(admin.site.urls)),
)
