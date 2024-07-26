from django.db import models

# Create your models here.
# customer/models.py

from django.db import models
from customers.models import Customer
from tablelist.models import TableList

class BookTable(models.Model):
    booktable_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(TableList, on_delete=models.CASCADE)
    booktable_date = models.DateField()  # Use DateField for dates
    booktable_time = models.TimeField()  # Use TimeField for times
    booktable_guests = models.PositiveIntegerField()  # Use PositiveIntegerField for number of guests

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.customer} on {self.booktable_date} at {self.booktable_time}"


