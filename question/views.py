from django.shortcuts import render
from .models import Question, Answer
from django.views.generic import ListView


# def question_list(request):
#     data = Question.objects.all()
    
#     context = {
#         'question_list': data
#     }

#     return render(request, 'question/question_list.html',context)

class Question_list(ListView):
    model  = Question


def question_detail(request, id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question=question)
    context = {
        'question':question,
        'answers' : answers,
    }
    return render(request, 'question/question_detail.html', context)