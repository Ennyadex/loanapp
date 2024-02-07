from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    updated_at = models.DateTimeField(null= True, auto_now= True)
    created_at = models.DateTimeField(null= True, auto_now= True)
    
    def __str__(self):
        return self.name
    
    
class Register(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    unique_no = models.CharField(max_length=10, default=None,null=True,blank=True)
    updateed_at = models.DateTimeField(null= True, auto_now= True)
    created_at = models.DateTimeField(null= True, auto_now= True)
    
class Login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    updated_at = models.DateTimeField(null= True, auto_now= True)
    created_at = models.DateTimeField(null= True, auto_now= True)
    
    