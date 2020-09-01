from django.db import models

# Create your models here.

class clients(models.Model):
    name = models.CharField(max_length=100)
    nif = models.IntegerField()
    date_birth = models.DateField(auto_now=False, auto_now_add=False)
    mail = models.EmailField(max_length=100)

class backlog(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    price = models.IntegerField()
    date_beg = models.DateField(auto_now=False, auto_now_add=True)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    days = models.IntegerField()

class catalog(models.Model):
    book = models.CharField(max_length=100)
    sort_of_book = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')