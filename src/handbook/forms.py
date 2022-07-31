from django import forms
from . import models

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class AddSerieForm(forms.ModelForm):
    class Meta:
        model = models.Bookseries
        fields = '__all__'
       
class AddGenreForm(forms.ModelForm):
    class Meta:
        model = models.Bookgenre
        fields = '__all__'

class AddPublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'