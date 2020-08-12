from django.http import Http404,HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_q_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'

    def get_queryset(self):

        return Question.objects.filter(pub_date__lte = timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


def vote(request,question_id):
    question = Question.objects.get(pk=question_id)
    try:
        print(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request, "poll/detail.html", {'error_message':"You didn't select a choice.",'question':question})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
