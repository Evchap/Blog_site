from django.db import models

class Musicians(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    audio = models.FileField(upload_to='audio/', blank=True)
    video = models.FileField(upload_to='video/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# $ python -m pip install Pillow
# $ python manage.py makemigrations
# $ python manage.py sqlmigrate musicians 0001 # посмотреть миграцию
# $ python manage.py migrate
