from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.TextField()

class Book(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.TextField()
    isbn = models.TextField()
    year = models.IntegerField()
