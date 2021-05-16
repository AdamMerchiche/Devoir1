from django.urls import path, re_path
from disks import views

urlpatterns = [
    path('accueil', views.lire_albums, name = "accueil"),
    path('track/<int:album_id>', views.afficher_tracks, name ="tracks"),
    path('album/recherche/<str:requete>', views.afficher_recherche, name ="albums"),
]

