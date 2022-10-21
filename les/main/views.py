from django.shortcuts import render, HttpResponse
from .models import getNews, getNewsById

# Create your views here.

def index(request):
    return render(request, "main/index.html", context={"news":getNews()})



def article(request, id):
    print()
    return render(request, "main/article.html", context={"news":getNewsById(id)[0]})