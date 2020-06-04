from django import forms
from django.shortcuts import render
from search.models import Author, Book

# Create your views here.
class Searchform(forms.Form):
    query = forms.CharField(max_length=128)

def index(request):
    #Render search form
    return render(request, "search/index.html", {
        "form": Searchform()
    })

def results(request):
    #Get values from form
    #Search for authors/books/isbn that match query
    form = Searchform(request.GET)
    if form.is_valid():
        query = form.cleaned_data["query"]
        authors = Author.objects.filter(name__icontains=query)[:10]
        titles = Book.objects.filter(title__icontains=query)[:10]
        isbns = Book.objects.filter(isbn__icontains=query)[:10]

        #Render view of all items matching query
        return render(request, "search/results.html", {
            "query":query,
            "authors": authors,
            "titles": titles,
            "isbns": isbns
        })

def author(request, author_id):
    #Get and render author info
    this_author = Author.objects.get(pk=author_id)
    books = this_author.books.all()
    return render(request, "search/author.html", {
        "author": this_author,
        "books": books
    })

def book(request, book_id):
    #Get and render book info
    this_book = Book.objects.get(pk=book_id)
    this_author = Author.objects.get(pk=this_book.author_id_id)
    return render(request, "search/book.html", {
        "book": this_book,
        "author": this_author
    })
