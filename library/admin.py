from django.contrib import admin
from library.models import Books, Loans, Customers
# Register your models here.
admin.site.register(Books)
admin.site.register(Customers)
admin.site.register(Loans)