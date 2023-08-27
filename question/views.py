from django.shortcuts import render
from .models import Question, Answer
from django.views.generic import ListView, DeleteView 

# def question_list(request):
#     data = Question.objects.all()
    
#     context = {
#         'question_list': data
#     }

#     return render(request, 'question/question_list.html',context)

class Question_list(ListView):
    model  = Question