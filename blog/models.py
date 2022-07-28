from statistics import quantiles
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Good(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    measure_unit = models.ForeignKey('Measure', on_delete=models.PROTECT)


    def __str__(self):
        return self.title


class Measure(models.Model):
    m_title = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.m_title


class Store(models.Model):
    store_name = models.CharField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.store_name


class Stock(models.Model):
    store_id = models.ForeignKey('Store', on_delete=models.PROTECT)
    good_id = models.ForeignKey('Good', on_delete=models.PROTECT)
    quantity_stock = models.DecimalField(max_digits=5, decimal_places=2)

    
    def __int__(self):
        return self.quantity_stock


class Order(models.Model):
    sender_store_id = models.CharField(max_length=100)
    recipient_store_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    quantity_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title