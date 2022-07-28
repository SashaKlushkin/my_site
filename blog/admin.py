from django.contrib import admin
from .models import Post, Good, Order, Measure, Stock, Store

admin.site.register(Post)
admin.site.register(Good)
admin.site.register(Measure)
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(Stock)