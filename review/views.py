from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def pro_index(request):
    return render(request, "review/pro_index.html")

def index(request):
    # review = Review.objects.order_by("-pk")
    return render(request, "review/index.html")
    
def genre(request):
    test = [0,1,2,3,4,5,6,7,8,9]
    context = {
        "test": test
    }
    return render(request, "review/genre.html", context)

# def create(request):

#     return render(request, "review/create.html")
# def detail(request):

#     return render(request, "review/detail.html")
