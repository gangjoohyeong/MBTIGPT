
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Chatroom, Qna
from chat.gpt import gpt_prompt
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import ChatroomForm




@login_required(login_url='common:login')
def index(request):
    chatroom_list = Chatroom.objects.filter(user=request.user).order_by('-create_date')
    context = {'chatroom_list': chatroom_list}
    return render(request, 'chat/chatroom_list.html', context)

@login_required(login_url='common:login')
def detail(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom.objects.filter(user=request.user), pk=chatroom_id)
    context = {'chatroom': chatroom}
    return render(request, 'chat/chatroom_detail.html', context)


@csrf_exempt
@login_required(login_url='common:login')
def qna_create(request, chatroom_id):
    if request.method == "POST":
        chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
        user = request.user
        qna_count = Qna.objects.filter(chatroom_id=chatroom.id).count()
        latest_qnas = Qna.objects.filter(chatroom_id=chatroom.id).order_by('-create_date')[:min(qna_count, 4)]
        qna_pairs = [(qna.question, qna.answer) for qna in latest_qnas]
        question = request.POST.get('question')
        answer = gpt_prompt(question, chatroom.title, chatroom.mbti, qna_pairs, user.last_name)
        qna = Qna(chatroom=chatroom, question=question, answer=answer, create_date=timezone.now(), user=user)
        qna.save()

        # JSON 형식으로 반환
        return JsonResponse({"answer": answer})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
    

@login_required(login_url='common:login')
def chatroom_create(request):
    if request.method == 'POST':
        form = ChatroomForm(request.POST)
        if form.is_valid():
            chatroom = form.save(commit=False)
            chatroom.user = request.user  # user 속성에 로그인 계정 저장
            chatroom.create_date = timezone.now()
            chatroom.save()
            return redirect('chat:index')
    else:
        form = ChatroomForm()
    context = {'form': form}
    return render(request, 'chat/chatroom_form.html', context)