
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Band, Musician, Album, Song

# Create your views here.
class BandListView(ListView):
    model = Band
    template_name= 'home.html'
    context_object_name = 'bands'

def artist_detail(request, band_id):
    albums = Album.objects.filter(band__id=band_id)
    band = Band.objects.get(id=band_id)
    band_members = Musician.objects.filter(band__id=band_id)

    context = {
        'albums': albums,
        'band': band,
        'band_members': band_members
}
    return render(request, 'artist_detail.html', context)

def album_detail(request, album_id):
    albums = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album_id)
    # albums = Album.objects.filter(band__name='band_name')

    context = {
        'album': albums,
        'song': songs
}
    print(songs)
    return render(request, 'album_detail.html',context)

def song_detail(request, song_id):
    songs = Song.objects.filter(song=song_id)


    context = {
        'song' : songs

}
    print(songs)
    return render(request, 'song_detail.html', context)