from django.shortcuts import render
from .models import Question


def index(request):
    return render(request, 'index.html')


def exibir(request, question_id):
    question = get_question(question_id)
    return render(request, 'questions.html', {'question': question})


def get_question(question_id):
    if question_id == 1:
        return Question(id=1, question_text='Qual seu nome?', pub_date='05/04/19')
    elif question_id == 2:
        return Question(id=2, question_text='Qual sua idade?', pub_date='05/04/19')
    elif question_id == 3:
        return Question(id=3, question_text='Qual sua altura?', pub_date='05/04/19')
