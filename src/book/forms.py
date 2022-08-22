from django import forms
from . import models

class AddBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()