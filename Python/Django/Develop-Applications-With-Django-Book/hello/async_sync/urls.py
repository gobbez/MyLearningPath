from django.urls import path

from . import views

urlpatterns = [
    path('sync/', views.view_sync, name='sync'),
    path('async/', views.view_async, name='async'),
]