from django.shortcuts import render, redirect
from .models import Question, Choice


def index(request):
    return render(request, 'index.html',
                  {'questions': Question.objects.all().order_by('-pub_date')})


def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choices.all().order_by('-votes')
    return render(request, 'questions.html', {'question': question,
                                              'choices': choices})


def results(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choices.all().order_by('-votes')
    qtd_votes_question = 0
    for choice in choices:
        qtd_votes_question += choice.votes
    return render(request, 'results.html', {'question': question,
                                            'choices': choices,
                                            'qtd_votes_question': qtd_votes_question})


def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choices.all().order_by('-votes')
    try:
        choice = question.choices.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'questions.html', {'question': question,
                                                  'choices': choices,
                                                  'mensagem': "Selecione uma opção."})
    else:
        choice.votes += 1
        choice.save()
        return redirect('index')


def manage(request, question_id):
    question = Question.objects.get(id=question_id)
    in_choices = question.choices.all().order_by('-votes')
    out_choices = list(Choice.objects.all())

    for choice in in_choices:
        for choice2 in out_choices:
            if choice2.choice_text == choice.choice_text:
                out_choices.remove(choice2)
    return render(request, 'manage.html', {'question': question,
                                           'in_choices': in_choices,
                                           'out_choices': out_choices})


def remove(request, question_id, choice_id):
    question = Question.objects.get(id=question_id)
    choice = question.choices.get(id=choice_id)
    choice.delete()
    return exibir(request, question_id)


def alter_status(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choices.all().order_by('-votes')
    if question.closed:
        question.closed = False
    else:
        question.closed = True
    question.save()
    return render(request, 'questions.html', {'question': question,
                                              'choices': choices})


def add(request, question_id, choice_id):
    question = Question.objects.get(id=question_id)
    choice = Choice.objects.get(id=choice_id)
    Choice.objects.create(choice_text=choice.choice_text, question=question)
    return exibir(request, question_id)
