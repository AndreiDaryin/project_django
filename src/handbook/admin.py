from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Author)
admin.site.register(models.Bookseries)
admin.site.register(models.Bookgenre)
admin.site.register(models.Publisher)