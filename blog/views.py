from django.shortcuts import render
from .models import Good, Post, Measure, Stock
from django.db.models import Sum


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# def sklad(request):
#     context = {
#         # 'goods': Good.objects.all(),
#         'stocks': Stock.objects.all()
#         # 'stocks': Stock.objects.aggregate(Sum('quantity_stock'))
#     }
#     return render(request, 'blog/sklad.html', context)

def sklad(request):
    prods = Good.objects.all()
    list_prod = []
    for prod in prods:
        print(prod.title)
        q_sum = Stock.objects.filter(good_id=prod) 
        # print(q_sum)
        qq_sum = q_sum.aggregate(Sum('quantity_stock'))
        print(qq_sum)
        list_prod.append({
            'name_prod' : prod.title,
            'qq_sum' : qq_sum['quantity_stock__sum']
            })
    print(list_prod)
    context = {
        'prods': list_prod
    }
    return render(request, 'blog/sklad.html', context)


# def sklad(request):
#     products = Good.objects.all()
#     prod_stock = Stock.objects.all()
#     for product in products:
#         # Stock.objects.filter(good_id=product.id)
#         field_name_sum = Stock.objects.aggregate(Sum('quantity_stock'))
#         # product.title

#         context = {
#      'field_name_sum': field_name_sum 
#     }
#     return render(request, 'blog/sklad.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})