from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from . import models
from . import forms


class BookList(generic.ListView):
    template_name = 'book//book_list.html'
    model = models.Book

class BookView(generic.DetailView):
    template_name = 'book//book_card.html'
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

class BookSearch(generic.ListView):
    template_name = 'book//book_search.html'
    model = models.Book
    def get_queryset(self):
        q = self.request.GET.get('search_query')
        if q:
            qs = self.model.objects.filter(Q(name__contains=q) |
                Q(author__surname__contains=q) | Q(seria__name__contains=q) |
                Q(genre__name__contains=q) | Q(publisher__name__contains=q))
        else:
            qs = []
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        q = self.request.GET.get('search_query', '')
        context['search_query'] = q
        return context
