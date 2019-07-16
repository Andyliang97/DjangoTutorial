from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    ##output = ','.join([question.question_text for question in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'you didn\'t a selection'})
    else:
        print(selected_choice.votes)
        selected_choice.votes = F('votes') + 1
        print(selected_choice.votes)  # F(votes) + Value(1)
        # selected_choice.votes += 1 this will get into race condition
        selected_choice.save()
        selected_choice.refresh_from_db()  # To access the new value saved this way, the object must be reloaded
        print(selected_choice.votes)
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
