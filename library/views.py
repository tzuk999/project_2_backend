from django.http import HttpResponse,JsonResponse
from library.models import Books,Customers,Loans
import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the library index.")

def books_json(books_objects):
    all_books = books_objects
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
    return json_data
#books
def books(request):
    all_books =  Books.objects.all()
    json_data = books_json(all_books)

    # Return the JSON response with the appropriate Content-Type header
    return JsonResponse(json_data, safe=False)

def books_name(request, name):
    all_books = Books.objects.filter(Q(name__iexact=name))
    json_data = books_json(all_books)
    return JsonResponse(json_data, safe=False)


#loans
def loans_json(loans_objects):
    all_loans = loans_objects
    loans_data = []
    for loan in all_loans:
        loan_data = {
            'id': loan.id,
            'customer': loan.customer.username,
            'book': loan.book.name,
            'loan_date': loan.loan_date,
            'return_date': loan.return_date,
            'status': loan.get_status_display()
        }
        loans_data.append(loan_data)
    json_data = json.dumps(loans_data)
    return json_data


def loans(request):
    all_loans = Loans.objects.all()
    json_data = loans_json(all_loans)
    return JsonResponse(json_data, safe=False)


def loans_by_customer(request, customer_id):
    all_loans = Loans.objects.filter(customer_id = customer_id)
    json_data = loans_json(all_loans)
    return JsonResponse(json_data, safe=False)



def customers_json(customers_objects):
    all_customers = customers_objects
    customers_data = []
    for customer in all_customers:
        customer_data = {
            'id' : customer.id,
            'name' : customer.username,
            'city' : customer.city,
            'age' : customer.age,
            'email' : customer.email
        }
        customers_data.append(customer_data)
    json_data = json.dumps(customers_data)
    return json_data


def all_customers(request):
    all_customers = Customers.objects.all()
    json_data = customers_json(all_customers)
    return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_customer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            username = data.get("username")
            email = data.get("email")
            city = data.get("city")
            age = data.get("age")
            password = data.get("password")

            # Create the customer
            customer = Customers.objects.create_user(username=username, email=email, city=city, age=age, password=password)

            return JsonResponse({"message": "Customer created successfully."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Method not allowed."}, status=405)


@csrf_exempt
def mylogin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            username = data.get("username")
            password = data.get("password")

            # Authenticate the user
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Login the user and store user ID in the session
                login(request, user)

                return JsonResponse({
                    "isAuthenticated": True,
                    "username": user.username,
                    "userId": user.id 
                })
            else:
                return JsonResponse({"error": "Invalid credentials."}, status=401)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Method not allowed."}, status=405)


def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})

