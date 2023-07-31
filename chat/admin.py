from django.contrib import admin
from .models import Chatroom

class ChatroomAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Chatroom, ChatroomAdmin)