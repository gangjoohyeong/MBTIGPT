from django import forms
from .models import Chatroom

class ChatroomForm(forms.ModelForm):
    MBTI_CHOICES = (
        ('ISTJ', 'ISTJ'),
        ('INTP', 'INTP'),
        ('ENFP', 'ENFP'),
        ('ENTJ', 'ENTJ'),
    )
    mbti = forms.ChoiceField(choices=MBTI_CHOICES)
    
    class Meta:
        model = Chatroom
        fields = ['title', 'mbti']