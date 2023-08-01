from django.contrib import admin
from library.models import Books, Loans, Customers
from django.contrib.auth.admin import UserAdmin
# Register your models here.

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'age', 'city')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(Books)
admin.site.register(Customers, UserAdmin)
admin.site.register(Loans)