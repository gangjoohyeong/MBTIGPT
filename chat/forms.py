from django import forms
from chat.models import Chatroom

class ChatroomForm(forms.ModelForm):
    MBTI_CHOICES = [
        ('ISTJ', 'ISTJ'),
        ('ENFP', 'ENFP'),
    ]

    mbti = forms.ChoiceField(choices=MBTI_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Chatroom
        fields = ['title', 'mbti']
