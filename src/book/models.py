from django.db import models
from handbook import models as hb_models
from datetime import datetime

class Book(models.Model):
    name = models.CharField(
        verbose_name="Book's name",
        max_length=50
    )
    foto = models.ImageField(
        upload_to='users/', 
        blank=True, 
        null=True,
    )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
    )
    author = models.ForeignKey(
        hb_models.Author,
        on_delete=models.PROTECT,
        verbose_name="Author",
        related_name='authors',
    )
    seria = models.ForeignKey(
        hb_models.Bookseries,
        on_delete=models.PROTECT,
        verbose_name="Seria",
        related_name='series',
    )
    genre = models.ForeignKey(
        hb_models.Bookgenre,
        on_delete=models.PROTECT,
        verbose_name="Genre",
        related_name='genres',
    )
    publisher = models.ForeignKey(
        hb_models.Publisher,
        on_delete=models.PROTECT,
        verbose_name="Publisher",
        related_name='publishers',
    )
    year = models.IntegerField(
        verbose_name="Year",
        blank=True, 
        null=True,
    )
    number_of_pages = models.IntegerField(
        verbose_name="Pages",
        blank=True, 
        null=True,
    )
    cover = models.CharField(
        verbose_name="Cover",
        max_length=15,
        blank=True, 
        null=True,
    )
    bookformat = models.CharField(
        verbose_name="Bookformat",
        max_length=20,
        blank=True, 
        null=True,
    )
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=25,
        blank=True, 
        null=True,
    )
    weight = models.IntegerField(
        verbose_name="Weight",
        blank=True, 
        null=True,
    )
    restrictions = models.IntegerField(
        verbose_name="Restrictions",
        blank=True, 
        null=True,
    )
    number_of_books = models.IntegerField(
        verbose_name="Number of books",
        blank=True, 
        null=True,
    )
    activity = models.CharField(
        verbose_name="Active y/n",
        max_length=20,
        choices=(('Y','Yes'), ('N','No'))
    )
    rating = models.IntegerField(
        verbose_name="Rating",
        blank=True, 
        null=True,
    )
    date_of_creation = models.DateField(
        verbose_name="Date of creation",
        auto_now_add=True
    )
    date_of_edit = models.DateField(
        verbose_name="Date of edit",
        auto_now=True
    )




   
    def __str__ (self) -> str:
        return self.name