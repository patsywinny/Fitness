from django.db import models


# Create your models here.
class member(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    repeat_password = models.CharField(max_length=20)
   

    def __str__(self):
        return self.fullname
    

# log in model
class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
   
    def __str__(self):
        return self.email
    

# contact us
class contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=300)
   

    def __str__(self):
        return self.username