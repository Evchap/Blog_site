from django.contrib import admin
from musicians.views import *
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicians.urls')),

]

handler404 = pageNotFound
