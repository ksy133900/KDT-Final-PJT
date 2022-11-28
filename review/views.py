from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def pro_index(request):
    return render(request, "review/pro_index.html")

def index(request):
    # review = Review.objects.order_by("-pk")
    return render(request, "review/index.html")


# def create(request):

#     return render(request, "review/create.html")
# def detail(request):

#     return render(request, "review/detail.html")
