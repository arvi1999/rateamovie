from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import MovieViewSet, RatingViewSet, UserViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
