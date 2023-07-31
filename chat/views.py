from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Chatroom, Qna
from chat.gpt import gpt_prompt





def index(request):
    chatroom_list = Chatroom.objects.order_by('-create_date') # '-': 역방향
    context = {'chatroom_list': chatroom_list}
    return render(request, 'chat/chatroom_list.html', context)

def detail(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    context = {'chatroom': chatroom}
    return render(request, 'chat/chatroom_detail.html', context)

def qna_create(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    # chatroom.qna_set.create(question=request.POST.get('question'), answer='더미 answer', create_date=timezone.now())
    
    question = request.POST.get('question')
    answer = gpt_prompt(question)
    
    qna = Qna(chatroom=chatroom, question=question, answer=answer, create_date=timezone.now())
    qna.save()
    
    return redirect('chat:detail', chatroom_id=chatroom.id)