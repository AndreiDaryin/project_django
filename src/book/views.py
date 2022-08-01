from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


class BookList(generic.ListView):
    template_name = 'book//book_list.html'
    model = models.Book

class BookDetailView(generic.DetailView):
    template_name = 'book//book_view.html'
    model = models.Book

class BookAdd(LoginRequiredMixin, generic.CreateView):
    template_name = 'book//book_add.html'
    model = models.Book
    form_class = forms.AddBookForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("book:book-det", kwargs={'pk': self.object.pk})  
    
class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'book//book_delete.html'
    model = models.Book
    success_url = reverse_lazy("book:book-list")
    login_url = reverse_lazy("account:user-login")

class BookEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'book//book_edit_view.html'
    model = models.Book
    form_class = forms.AddBookForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("book:book-det", kwargs={'pk': self.object.pk})