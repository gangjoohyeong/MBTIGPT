from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:chatroom_id>/', views.detail, name='detail'),
]