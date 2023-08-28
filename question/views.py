from django.shortcuts import render
from .models import Question, Answer
from django.views.generic import ListView
from .forms import AnswerForm

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

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.question = question
            form.author = request.user
            form.save()
    else:
        form = AnswerForm()

    context = {
        'question':question,
        'answers' : answers,
        'form' : form
    }
    return render(request, 'question/question_detail.html', context)