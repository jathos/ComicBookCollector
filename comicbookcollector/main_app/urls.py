from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comics/', views.comics_index, name='index'),
    path('comics/<int:comic_id>', views.comic_details, name='details'),
    path('comics/create/', views.ComicCreate.as_view(), name='comics_create'),
    path('comics/<int:pk>/update/', views.ComicUpdate.as_view(), name='comics_update'),
    path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comics_delete'),
    path('comics/<int:comic_id>/add_reading/', views.add_reading, name='add_reading'),
    path('comics/<int:comic_id>/assoc_artist/<int:artist_id>/', views.assoc_artist, name='assoc_artist'),
    path('comics/<int:comic_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]