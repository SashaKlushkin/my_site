from django.shortcuts import render
from .models import Good, Post, Measure, Stock


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def sklad(request):
    context = {
        # 'goods': Good.objects.all(),
        'stocks': Stock.objects.all()
    }
    return render(request, 'blog/sklad.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})