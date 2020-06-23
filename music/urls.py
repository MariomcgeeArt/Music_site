from django.urls import path

from . import views

urlpatterns = [
  path('',views.artist_list_view, name='artist'),
  path('artist/<int:artist_id>/', views.artist_detail_view, name='artists'),
  path('album/<int:album_id>/', views.album_detail, name='album'),
  path('song/<int:song_id>/', views.song_detail, name='song'),
   
]