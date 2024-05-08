from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm


def list_questions(request):
    questions = Question.objects.all()
    args = {'questions': questions}
    return render(request, "path_to/file.html", args)


def add_question(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = QuestionForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect("questions_list") #TODO: Редирект на реальный url

    else:
        form = QuestionForm()

    context = {"form": form, "edit_mode":False}

    return render(request, "path_to/file.html", context) #TODO: Путь к реальному файлу html