from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:book_id>", views.edit, name="edit"),
    path("new/<int:book_id>", views.new, name="new")
    
]
