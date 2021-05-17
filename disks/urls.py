from django.urls import path, re_path
from disks import views

urlpatterns = [
    path('accueil', views.lire_albums, name = "accueil"),
    path('', views.lire_albums, name="home2"),
    path('track/<int:album_id>', views.afficher_tracks, name ="tracks"),
    path('album/recherche', views.afficher_recherche, name ="albums"),
]

