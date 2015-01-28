from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from web import views

urlpatterns = patterns('',
    url(r'^bill/$', views.BillList.as_view()),
    url(r'^bill/(?P<pk>[0-9]+)/$', views.BillDetail.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
