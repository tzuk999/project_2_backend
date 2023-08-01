from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.books, name="books"),
    path("books/<name>", views.books_name, name="books_name"),
    path("loans", views.loans, name="loans"),
    path("customers", views.customers, name="customers")
]