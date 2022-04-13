from django.urls import path
from .views import *

urlpatterns = [
	path('genre', genre_json),
	path("genre/<int:id>", genre_json_individual),
	path('artist', artist_json),
	path("artist/<int:id>", artist_json_individual),
	path('album', album_json),
	path("album/<int:id>", album_json_individual),
	path('song', song_json),
	path("song/<int:id>", song_json_individual),
]
