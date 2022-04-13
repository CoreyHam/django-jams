from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Genre, Artist, Album, Song
# Create your views here.

def genre_json(request):
	x = Genre.objects.all().values()
	data = list(x)
	return JsonResponse({ 'data': data })

def genre_json_individual(request, id):
	x = Genre.objects.filter(id=id).values()
	data = list(x)
	return JsonResponse({ 'data': data })

def artist_json(request):
	x = Artist.objects.all().values()
	data = list(x)
	return JsonResponse({ 'data': data })

def artist_json_individual(request, id):
	x = Artist.objects.filter(id=id).values()
	data = list(x)
	return JsonResponse({ 'data': data })

def album_json(request):
	x = Album.objects.all().values()
	data = list(x)
	return JsonResponse({ 'data': data })

def album_json_individual(request, id):
	x = Album.objects.filter(id=id).values()
	data = list(x)
	return JsonResponse({ 'data': data })

def song_json(request):
	x = Song.objects.all().values()
	data = list(x)
	return JsonResponse({ 'data': data })

def song_json_individual(request, id):
	x = Song.objects.filter(id=id).values()
	data = list(x)
	return JsonResponse({ 'data': data })