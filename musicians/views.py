from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse("Страница приложения musicians.")


def categories(request, catid):
    # if request.GET:
    #     print(request.GET)
    # if request.POST:
    #     print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2022:
        # raise Http404()
        # return redirect('/') # 302 redirect временное перемещение на страницу
        # return redirect('/', permanent=True) # 301 redirect постоянное перемещение
        return redirect('home', permanent=True)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

