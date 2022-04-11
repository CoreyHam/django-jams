from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=30)

class Artist(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    active_from = models.IntegerField(null=True, blank=True)
    monthly_listeners = models.IntegerField(default=0)

class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)
    song_total = models.IntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)


class Song(models.Model):
    title = models.CharField(max_length=30)
    artist = models.ManyToManyField(Artist)
    album = models.ManyToManyField(Album)
    duration = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre)
    
