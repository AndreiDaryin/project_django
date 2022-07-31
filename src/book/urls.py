from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('book-list/', views.BookList.as_view(), name="book-list"),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name="book-det"),
    path('book-add/', views.BookAdd.as_view(), name="book-add"),
    path('book-delete/<int:pk>/', views.BookDeleteView.as_view(), name="book-del"),
    path('book-edit/<int:pk>/', views.BookEditView.as_view(), name="book-edit"),
]