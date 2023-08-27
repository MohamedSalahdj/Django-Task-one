from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    content = models.TextField(max_length=3000)
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    tag = TaggableManager()


class Answer(models.Model):
    answer = models.TextField(max_length= 3500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answer')
    created_at = models.DateTimeField(default=timezone.now)