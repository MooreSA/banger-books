from django.shortcuts import render
from django.forms import ModelForm
from search.models import Author, Book
from .models import Review
# Create your views here.

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']

def new(request, book_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            pass
    this_book = Book.objects.get(pk=book_id)
    this_author = Author.objects.get(pk=this_book.author_id_id)
    return render(request, "review/new.html", {
        "book": this_book,
        "author": this_author,
        "form": ReviewForm()
    })
