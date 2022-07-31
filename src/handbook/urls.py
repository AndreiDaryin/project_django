from django.urls import path
from . import views

app_name = 'handbook'
urlpatterns = [
    path('', views.handbook_view),
    path('author-list/', views.AuthorList.as_view(), name="auth-list"),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name="auth-det"),
    path('author-add/', views.AuthorAdd.as_view(), name="auth-add"),
    path('author-delete/<int:pk>/', views.AuthorDeleteView.as_view(), name="auth-del"),
    path('author-edit/<int:pk>/', views.AuthorEditView.as_view(), name="auth-edit"),
    path('bookserie-list/', views.BookseriesList.as_view(), name="serie-list"),
    path('bookserie/<int:pk>/', views.BookseriesDetailView.as_view(), name="serie-det"),
    path('bookserie-add/', views.BookseriesAdd.as_view(), name="serie-add"),
    path('bookserie-delete/<int:pk>/', views.BookseriesDeleteView.as_view(), name="serie-del"),
    path('bookserie-edit/<int:pk>/', views.BookseriesEditView.as_view(), name="serie-edit"),
    path('genre-list/', views.GenreList.as_view(), name="genre-list"),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name="genre-det"),
    path('genre-add/', views.GenreAdd.as_view(), name="genre-add"),
    path('genre-delete/<int:pk>/', views.GenreDeleteView.as_view(), name="genre-del"),
    path('genre-edit/<int:pk>/', views.GenreEditView.as_view(), name="genre-edit"),
    path('publisher-list/', views.PublisherList.as_view(), name="publisher-list"),
    path('publisher/<int:pk>/', views.PublisherDetailView.as_view(), name="publisher-det"),
    path('publisher-add/', views.PublisherAdd.as_view(), name="publisher-add"),
    path('publisher-delete/<int:pk>/', views.PublisherDeleteView.as_view(), name="publisher-del"),
    path('publisher-edit/<int:pk>/', views.PublisherEditView.as_view(), name="publisher-edit"),
]