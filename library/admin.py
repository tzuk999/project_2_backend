from django.contrib import admin
from library.models import Books, Loans, Customers
# Register your models here.
admin.register(Books)
admin.register(Customers)
admin.register(Loans)