from django.shortcuts import render, get_object_or_404
from .models import Chatroom

def index(request):
    chatroom_list = Chatroom.objects.order_by('-create_date') # '-': 역방향
    context = {'chatroom_list': chatroom_list}
    return render(request, 'chat/chatroom_list.html', context)

def detail(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    context = {'chatroom': chatroom}
    return render(request, 'chat/chatroom_detail.html', context)