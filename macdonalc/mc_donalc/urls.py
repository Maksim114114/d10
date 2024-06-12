from .views import IndexView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view())
]