from django.conf.urls import url, include

from rest_framework import routers
from .viewsets import index_viewset
from .views import index

router = routers.DefaultRouter()

router.register('api', index_viewset)
urlpatterns = [

    url(r'^myapp/', index),  # function based views
    url(r'^', include(router.urls)),


]