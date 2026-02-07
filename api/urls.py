from django.urls import path, include
from . import views

app_name = "api"

urlpatterns = [
    path("", views.index, name="index"),
    path("current-datetime/", views.current_datetime, name="current_datetime"),
]
