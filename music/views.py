from django.http import HttpResponse
from .models import Musician, Album, Song
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, world. This is my music site!")

def classical_songs(request):
    return HttpResponse("Hello Classical!")

def artist_list_view(request):
    context = {
    'artists': Musician.objects.all()
  }
    return render(request, 'artist_display.html', context)

     
# #todo: create new url path
def artist_detail_view(request,artist_id):
    artist= Musician.objects.get(id=artist_id)
    albums= artist.album_set.all()
    context = {
    'artist': artist,
    'albums': albums
  }
    return render(request, 'artist_detail.html', context)
    


def album_detail(request,album_id):
    album= Album.objects.get(id=album_id)
    song= album.song_set.all()
    context = {
    'album': album,
    'song': song

  }
    return render(request, 'album_detail.html', context)


def song_detail(request,song_id):
    song= Song.objects.get(id=song_id)
   
    context = {
        'song': song

  }
    return render(request, 'song_detail.html', context)
   





