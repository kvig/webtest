from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("lists", views.ListViewSet, basename="lists")
router.register("tasks", views.TaskViewSet, basename="tasks")

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
]

