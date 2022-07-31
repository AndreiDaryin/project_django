from django.db import models

# Create your models here.
class Author(models.Model):
    surname = models.CharField(
        verbose_name="Author's surname",
        max_length=25
    )
    name = models.CharField(
        verbose_name="Authors name",
        max_length=25
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )
    def __str__ (self) -> str:
        return self.surname

class Bookseries(models.Model):
    name = models.CharField(
        verbose_name="Bookseries",
        max_length=40
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )
    def __str__ (self) -> str:
        return self.name

class Bookgenre(models.Model):
    name = models.CharField(
        verbose_name="Bookgenre",
        max_length=25
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )
    def __str__ (self) -> str:
        return self.name

class Publisher(models.Model):
    name = models.CharField(
        verbose_name="Publisher",
        max_length=45
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )
    def __str__ (self) -> str:
        return self.name

