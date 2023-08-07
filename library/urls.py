from django.urls import path

from . import views

urlpatterns = [
    path('logout', views.logout_user, name='logout_user'),
    path('get_csrf_token', views.get_csrf_token, name='get_csrf_token'),
    path('login', views.mylogin, name='mylogin'),
    path("", views.index, name="index"),
    path("books", views.books, name="books"),
    path("books/<name>", views.books_name, name="books_name"),
    path("loans", views.loans, name="loans"),
    path("loans/<int:customer_id>", views.loans_by_customer, name="loans_by_customer"),
    path("customers", views.all_customers, name="all_customers"),
    path("create_customer", views.create_customer, name='create_customer')
]