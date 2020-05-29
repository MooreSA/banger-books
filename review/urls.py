from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("new/<int:book_id>", views.new, name="new")
]
