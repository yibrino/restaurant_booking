

from django.db import models

# customer/models.py
from user.models import AppUser
from django.db import models
class TableList(models.Model):
    table_id = models.AutoField(primary_key=True)  
    # admin_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    table_name= models.CharField(max_length=255)
    table_max_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table_name


