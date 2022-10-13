from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', MusiciansHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
#    path('post/<int:post_id>/', show_post, name='post'), # ссылка на список статей
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', MusiciansCategory.as_view(), name='category'),
]

# http://127.0.0.1:8000/about/


