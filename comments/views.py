from django.shortcuts import render, redirect

# Create your views here.
def comments(request,pk):
    return render(request, "comments/comments.html")