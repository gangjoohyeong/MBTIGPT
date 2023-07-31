from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:chatroom_id>/', views.detail),
]