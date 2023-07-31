from django.db import models


class Chatroom(models.Model):
    title = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class Qna(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    create_date = models.DateTimeField()




