from django.conf.urls.static import static
from django.urls import path, re_path

from Blogsite import settings
from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]

if settings.DEBUG: # только в режиме отладки к маршрутам строки 8-10 добавляется
    # маршрут к статическим файлам
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404=pageNotFound
