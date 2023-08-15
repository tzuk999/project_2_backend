from django.urls import path

from . import views

urlpatterns = [
    path("late_loans", views.late_loans, name="late_loans"),
    path("loans/delete/<int:loan_id>", views.delete_loan, name="delete_loan"),
    path("loans/book/<int:book_id>", views.loans_by_book, name="loans_by_book"),
    path("customers/<name>", views.customers_name, name="customers_name"),
    path('create_loan', views.create_loan, name='cteate_loan'),
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