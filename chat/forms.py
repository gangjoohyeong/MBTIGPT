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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = '친구 이름'
        self.fields['title'].widget = forms.TextInput()
        
        self.fields['mbti'].label = '친구의 MBTI' 