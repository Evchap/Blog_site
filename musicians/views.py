from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse("Страница приложения musicians.")


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

