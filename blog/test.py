
from django.shortcuts import render
from .models import Good, Post, Measure, Stock
from django.db.models import Sum

products = Good.objects.all()
prod_stock = Stock.objects.all()
for product in products:
        # Stock.objects.filter(good_id=product.id)
    field_name_sum = Stock.objects.aggregate(Sum(product.id))
    print(field_name_sum)

    