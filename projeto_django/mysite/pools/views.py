from django.shortcuts import render
from .models import Question, Choice


def index(request):
    return render(request, 'index.html',
                  {'questions': Question.objects.all().order_by('-pub_date'),
                   'choices': Choice.objects.all()})


def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'questions.html', {'question': question,
                                              'choices': Choice.objects.all()})


def results(request, question_id):
    pass
