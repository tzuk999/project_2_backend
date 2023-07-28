from django.db import models
from django.utils import timezone

# Create your models here.
class Books(models.Model):
    class BookTypeEnum(models.IntegerChoices):
        TEN_DAYS = 1
        FIVE_DAYS = 2
        TWO_DAYS = 3
    class StatusEnum(models.IntegerChoices):
        AVAILABLE = 1
        UNAVAILABLE = 2
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField(default= 0)
    book_type = models.IntegerField(choices=BookTypeEnum.choices)
    status = models.IntegerField(choices=StatusEnum.choices)


class Customers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField(default= 0)



class Loans(models.Model):
    class StatusEnum(models.IntegerChoices):
        ON_TIME = 1
        LATE = 2
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(default = timezone.now())
    return_date = models.DateTimeField(default= timezone.now())