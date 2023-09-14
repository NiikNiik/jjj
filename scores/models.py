from django.db import models



class User(models.Model):
    phone_number = models.CharField(max_length =100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

