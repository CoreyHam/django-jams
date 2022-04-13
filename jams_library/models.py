from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.genre

class Artist(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    active_from = models.IntegerField(null=True, blank=True)
    monthly_listeners = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)
    song_total = models.IntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=30)
    artist = models.ManyToManyField(Artist)
    album = models.ManyToManyField(Album)
    track = models.IntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    
