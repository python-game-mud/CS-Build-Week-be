from django.conf.urls import url
from . import api

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rooms', api.RoomViewSet)

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    # url("rooms", api.all_rooms),
    path('', include(router.urls)),
]