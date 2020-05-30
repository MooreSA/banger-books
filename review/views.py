from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from search.models import Author, Book
from django.shortcuts import render
from django.urls import reverse
from .models import Review
# Create your views here.

class ReviewForm(forms.Form):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=1024)
    rating = forms.IntegerField(max_value=5, min_value=0)

@login_required()
def new(request, book_id):
    #Get info from form
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            rating = form.cleaned_data["rating"]
            user_id = request.user.id
            book = Book.objects.get(pk=book_id)
            #Save info into  new review
            new_review = Review(title=title, content=content, rating=rating, user_id=user_id, book=book)
            new_review.save()

    #Check if user has already reviewed this book
    if Review.objects.filter(user_id=request.user.id).exists():
        return HttpResponseRedirect(reverse('users:index'))

    #Render view for new review
    this_book = Book.objects.get(pk=book_id)
    this_author = Author.objects.get(pk=this_book.author_id_id)
    return render(request, "review/new.html", {
        "book": this_book,
        "author": this_author,
        "form": ReviewForm()
    })
