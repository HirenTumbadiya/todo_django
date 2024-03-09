from django.contrib import admin
from django.urls import path, include
from api.views import TaskViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
# Task site
    path('', include(router.urls))
]