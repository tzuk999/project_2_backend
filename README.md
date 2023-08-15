Librery
Models:
  Books:
  - name
  - author
  - year of publish
  - book type (choise out of three typse from enum class that set the time of the loan)
  - status (create and changes automaticaly by the availability of the book)

  Customers (django users):
  (additions to the basic django user model)
  - city
  - age

  Loans:
  - customer (Customers FK)
  - book (Books FK)
  - loan date (the time when the book got loaned)
  - return date (the time that the customer need to return the book, determined by the book type)
  - status (create and changes automaticaly, checking if the return time has past and the customer is late)

  routes:
  - ./library/late_loans (GET) -
    get all late loans
  - ./library/loans/delete/<loan_id> (DELETE) - 
    delete a given loan
  - ./library/loans/<customer_id> (GET) -
    get all loan of the given customer
  - ./library/loans/book/<book_id> (GET) -
    get the loan of the given book
  - ./library/loans (GET) -
    get all loans
  - ./library/create_loan (POST) -
    create a new loan, need to receive customer id and book id
  - ./library/customers/<name> (GET) -
    get customers by a given username 
  - ./library/customers (GET) -
    get all customers
  - ./library/create_customer (POST) -
    creating a new customer (user), need to receive username, email, city, age, and password
  - ./library/books (GET) -
    get all books
  - ./library/books/<name> (GET) -
    get books by a given name
  - ./library/login (POST) -
    login to django, need to get username and password
  - ./library/logout (POST) -
    logout from django
  - ./library/get_csrf_token (GET) -
    get csrf token from django
