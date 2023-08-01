from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse





def index(request):

    return render(request, 'main.html')