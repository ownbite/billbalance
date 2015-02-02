from django.contrib import admin
from web import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'bills', views.BillViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'nodes', views.NodeViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
