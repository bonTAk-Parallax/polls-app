from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choices
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q

# Create your views here.
# class CustomGenericeViewSet(generic.ListView, generic.CreateView, generic.UpdateView, generic.DeleteView):
#     pass 

class IndexView(generic.ListView):
    template_name = "polls_app/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(
            question_choies__isnull=False,
            pub_date__lte=timezone.now(),
            ).distinct().order_by("pub_date")[:5]
        #  return Question.objects.filter(
        #     pub_date__lte=timezone.now(),
        #     ).order_by("pub_date")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls_app/detail.html"

    def get_queryset(self):
        return Question.objects.filter(
            question_choies__isnull = False,
            pub_date__lte = timezone.now()).distinct()

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls_app/results.html"

    def get_queryset(self):
        return Question.objects.filter(
            question_choies__isnull = False,
            pub_date__lte = timezone.now()).distinct()


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.question_choies.get(pk=request.POST["choice"])
    except (KeyError, Choices.DoesNotExist):
        return render(
            request,
            "polls_app/detail.html",
            {
                "question": question,
                "error_message": "Your didn't select a choice."
            },
        )
    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls_app:results", args=(question.id,)))





# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     # output = ",".join([q.question_text for q in latest_question_list])
#     return render(request, "polls_app/index.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls_app/detail.html", {'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls_app/results.html", {"question": question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choices_set.get(pk=request.POST["choice"])
#     except (KeyError, Choices.DoesNotExist):
#         return render(
#             request,
#             "polls_app/detail.html",
#             {
#                 "question": question,
#                 "error_message": "Your didn't select a choice."
#             },
#         )
#     else:
#         selected_choice.votes = F("votes")+1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse("polls_app:results", args=(question.id,)))
