from django.contrib import admin
from .models import Genre, Song, Artist, Album
# Register your models here.
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)