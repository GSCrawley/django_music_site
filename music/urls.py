from django.urls import path
from .views import BandListView, ListView
from music.views import artist_detail, album_detail, song_detail


urlpatterns =[
    path('', BandListView.as_view(), name='home'),
    path('artist/<int:band_id>/', artist_detail, name='artist_detail'),
    path('album/<int:album_id>/album', album_detail, name='album_detail'),
    path('song/<int:song_id>/song', song_detail, name='song_detail')
]