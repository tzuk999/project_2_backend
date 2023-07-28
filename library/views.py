from django.http import HttpResponse,JsonResponse
from library.models import Books,Customers,Loans
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the library index.")
#books
def books(request):
    all_books =  Books.objects.all()
    books_data = []
    for book in all_books:
        book_data = {
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'year_published': book.year_published,
            'book_type': book.get_book_type_display(),  # Use the display name of the enum choice
            'status': book.get_status_display()        # Use the display name of the enum choice
        }
        books_data.append(book_data)

    # Serialize the list of dictionaries into a JSON string
    json_data = json.dumps(books_data)

    # Return the JSON response with the appropriate Content-Type header
    return JsonResponse(json_data, safe=False)


#loans
def loans(request):
    all_loans = Loans.objects.all()
    loans_data = []
    for loan in all_loans:
        loan_data = {
            'id': loan.id,
            'customer': loan.customer,
            'book': loan.book,
            'loan_date': loan.loan_date,
            'return_date': loan.return_date,
            'status': loan.get_status_display()
        }
        loans_data.append(loan_data)
    json_data = json.dumps(loans_data)
    return JsonResponse(json_data, safe=False)


def customers(request):
    all_customers = Customers.objects.all()
    customers_data = []
    for customer in all_customers:
        customer_data = {
            'id' : customer.id,
            
        }