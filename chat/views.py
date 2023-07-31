from django.http import HttpResponse

def index(request):
    return HttpResponse("이곳은 채팅 메인 페이지입니다.")