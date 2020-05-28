from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.TextField()
    isbn = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return f"'{self.title}', written in {self.year}. ISBN: {self.isbn}"
