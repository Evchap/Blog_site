from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import * # импорт моделей

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Musicians.objects.all()
#    cats = Category.objects.all()

    context = {
        'posts': posts,
#        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'musicians/index.html', context=context)


def about(request):
    return render(request, 'musicians/about.html', {'menu': menu, 'title': 'О сайте'})


# def addpage(request):
# #    return HttpResponse("Добавление статьи")
#     form = AddPostForm()
#     return render(request, 'musicians/addpage.html', {'form': menu, 'title': 'Добавление статьи', 'form': form})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'musicians/addpage.html', {'form': menu, 'title': 'Добавление статьи', 'form': form})


def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_id):
#     return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_post(request, post_slug):
#     post = get_object_or_404(Musicians, pk=post_id)
    post = get_object_or_404(Musicians, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': 1,
    }

    return render(request, 'musicians/post.html', context=context)

def show_category(request, cat_id):
    posts = Musicians.objects.filter(cat_id=cat_id)
#    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
#        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }

    return render(request, 'musicians/index.html', context=context)

