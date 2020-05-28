from django.urls import path

from . import views

app_name = "search"

urlpatterns = [
    path("", views.index, name="index"),
    path("author/<int:author_id>", views.author, name="author"),
    path("results", views.results, name="results"),
    path("book/<int:book_id>", views.book, name="book")
]
