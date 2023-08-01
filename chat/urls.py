from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:chatroom_id>/', views.detail, name='detail'),
    path('qna/create/<int:chatroom_id>', views.qna_create, name='qna_create'),
    path("qna_create_ajax/<int:chatroom_id>/", csrf_exempt(views.qna_create), name="qna_create_ajax"),
    path('chatroom/create/', views.chatroom_create, name='chatroom_create'),
]