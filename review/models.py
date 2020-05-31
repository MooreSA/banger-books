from django.db import models
from django.core.validators import MaxValueValidator
from search.models import Book
# Create your models here.

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    title = models.TextField(max_length=128)
    user_id = models.IntegerField()
    content = models.TextField(max_length=1024)
    rating = models.SmallIntegerField(default=3, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"Review of {self.book}, {self.rating} out of 5"
