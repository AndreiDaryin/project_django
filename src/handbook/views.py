from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic 
from . import models
from . import forms
from book import models as b_models
from datetime import datetime, timedelta

fivedays = timedelta(days = 5)

# Create your views here.
def handbook_view(request):
    return HttpResponse("<h1>This is our handbook. Here you can find everything you want</h1>")

class HomePage(generic.TemplateView):
    template_name = 'handbook\home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['genre_list'] = models.Bookgenre.objects.all()
        context['publisher_list'] = models.Publisher.objects.all()
        context['author_list'] = models.Author.objects.all()
        context['new_books'] = b_models.Book.objects.filter(date_of_creation__gt=datetime.now() - fivedays).reverse()[:3:]
        context['best_books'] = b_models.Book.objects.filter(rating__gte=9).reverse()[:3:]
        context['discount'] = b_models.Book.objects.filter(price__lte=10).reverse()[:3:]
        return context


    
class AuthorList(generic.ListView):
    template_name = 'handbook\\author_list.html'
    model = models.Author

class AuthorDetailView(generic.DetailView):
    template_name = 'handbook\\author_view.html'
    model = models.Author

class AuthorAdd(LoginRequiredMixin, generic.CreateView):
    template_name = 'handbook\\author_add.html'
    model = models.Author
    form_class = forms.AddAuthorForm
    login_url = reverse_lazy("account:user-login")

    def get_success_url(self):
        return reverse_lazy("handbook:auth-det", kwargs={'pk': self.object.pk})  
    
class AuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'handbook\\author_delete.html'
    model = models.Author
    success_url = reverse_lazy("handbook:auth-list")
    login_url = reverse_lazy("account:user-login")

class AuthorEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'handbook\\author_edit_view.html'
    model = models.Author
    form_class = forms.AddAuthorForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("handbook:auth-det", kwargs={'pk': self.object.pk})
        #return f"/handbook/author/{self.object.pk}/"  


class BookseriesList(generic.ListView):
    template_name = 'handbook\\bookserie_list.html'
    model = models.Bookseries
class BookseriesDetailView(generic.DetailView):
    template_name = 'handbook\\bookserie_view.html'
    model = models.Bookseries

class BookseriesAdd(LoginRequiredMixin, generic.CreateView):
    template_name = 'handbook\\bookserie_add.html'
    model = models.Bookseries
    form_class = forms.AddSerieForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("handbook:serie-det", kwargs={'pk': self.object.pk})
       
    
class BookseriesDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'handbook\\bookserie_delete.html'
    model = models.Bookseries
    success_url = reverse_lazy("handbook:serie-list")
    login_url = reverse_lazy("account:user-login")

class BookseriesEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'handbook\\bookserie_edit_view.html'
    model = models.Bookseries
    form_class = forms.AddSerieForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("handbook:serie-det", kwargs={'pk': self.object.pk})
        #return f"/handbook/author/{self.object.pk}/"

class GenreList(generic.ListView):
    template_name = 'handbook\\genre_list.html'
    model = models.Bookgenre
class GenreDetailView(generic.DetailView):
    template_name = 'handbook\\genre_view.html'
    model = models.Bookgenre

class GenreAdd(LoginRequiredMixin, generic.CreateView):
    template_name = 'handbook\\genre_add.html'
    model = models.Bookgenre
    form_class = forms.AddGenreForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("handbook:genre-det", kwargs={'pk': self.object.pk})
       
    
class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'handbook\\genre_delete.html'
    model = models.Bookgenre
    success_url = reverse_lazy("handbook:genre-list")
    login_url = reverse_lazy("account:user-login")

class GenreEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'handbook\\genre_edit_view.html'
    model = models.Bookgenre
    form_class = forms.AddGenreForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("handbook:genre-det", kwargs={'pk': self.object.pk})
        #return f"/handbook/author/{self.object.pk}/"

class PublisherList(generic.ListView):
    template_name = 'handbook\\publisher_list.html'
    model = models.Publisher
class PublisherDetailView(generic.DetailView):
    template_name = 'handbook\\publisher_view.html'
    model = models.Publisher

class PublisherAdd(LoginRequiredMixin, generic.CreateView):
    template_name = 'handbook\\publisher_add.html'
    model = models.Publisher
    form_class = forms.AddPublisherForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("handbook:publisher-det", kwargs={'pk': self.object.pk})
       
    
class PublisherDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'handbook\\publisher_delete.html'
    model = models.Publisher
    success_url = reverse_lazy("handbook:publisher-list")
    login_url = reverse_lazy("account:user-login")

class PublisherEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'handbook\\publisher_edit_view.html'
    model = models.Publisher
    form_class = forms.AddPublisherForm
    login_url = reverse_lazy("account:user-login")
    
    def get_success_url(self):
        return reverse_lazy("handbook:publisher-det", kwargs={'pk': self.object.pk})
        #return f"/handbook/author/{self.object.pk}/"