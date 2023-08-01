from django.db import models
from django.contrib.auth.models import User

class Chatroom(models.Model):
    title = models.TextField()
    create_date = models.DateTimeField()
    mbti = models.CharField(max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Qna(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()




