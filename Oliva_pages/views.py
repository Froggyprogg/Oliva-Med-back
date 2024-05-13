from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from Oliva_pages.forms import ReviewForm
from Oliva_pages.models import Doctor, News, MedicalService, CalendarEvents


def add_review(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReviewForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect("questions_list") #TODO: Редирект на реальный url

    else:
        form = ReviewForm()

    context = {"form": form, "edit_mode":False}

    return render(request, "path_to/file.html", context) #TODO: Путь к реальному файлу html


def list_doctors(request): #TODO: нужно добавить во view главной страницы
    doctors = Doctor.objects.all()
    args = {'questions': doctors}
    return render(request, "path_to/file.html", args) #TODO: Путь к реальному файлу html


def list_news(request): #TODO: нужно добавить во view главной страницы
    news = News.objects.all()
    args = {'questions': news}
    return render(request, "path_to/file.html", args) #TODO: Путь к реальному файлу html


def list_medicalservice(request): #TODO: нужно добавить во view главной страницы
    service = MedicalService.objects.all()
    args = {'questions': service}
    return render(request, "path_to/file.html", args) #TODO: Путь к реальному файлу html


def list_calendarevents(request): #TODO: нужно добавить во view главной страницы
    events = CalendarEvents.objects.all()
    args = {'questions': events}
    return render(request, "path_to/file.html", args) #TODO: Путь к реальному файлу html