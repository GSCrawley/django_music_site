from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Band, Musician, Album, Song

# Create your views here.
class BandListView(ListView):
    model = Band
    template_name= 'home.html'
    context_object_name = 'bands'

    def artist_detail(self, request, band_id):
        albums = Album.objects.filter(band__id=band_id)
        artist = Band.objects.get(id=band_id)
    
        context = {
            'albums': albums,
            'bands': artist
    }
        return render(request, 'artist_detail.html', context)

    def album_detail(self, request, album_id):
        albums = Album.objects.get(id=album_id)
        songs = Song.objects.filter(album=album_id)
    # albums = Album.objects.filter(artist__name='artist_name')

        context = {
         'album': albums, 
         'song': songs
    }
        return render(request, 'album_detail.html',context)

    def song_detail(self, request, song_id):
        songs = Song.objects.get(id=song_id)

        context = {
            'song' : songs
    }
        return render(request, 'song_detail.html', context)
