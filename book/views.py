from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def create(request):
    if request.method == "POST":
        book_form = bookForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        # images = request.FILES.getlist("image")

        if book_form.is_valid() and image_form.is_valid():
            book = book_form.save(commit=False)
            book.user = request.user
            book.save()
            images = image_form.save(commit=False)
            images.book = book
            images.save()
            
            # if len(images):
            #     for img in images:
            #         img_instance = Image(book=book, image=img)

            #         img_instance.save()

            return redirect("review:index")
    else:
        book_form = bookForm()
        image_form = ImageForm()
    context = {
        "book_form": book_form,
        "image_form": image_form,
    }
    return render(request, "book/create.html", context)

def delete(request,book_pk):
    book = Book.objects.get(pk = book_pk)
    book.delete()
    return redirect("review:index")