from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def create(request):
    if request.method == "POST":
        book_form = bookForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        images = request.FILES.getlist("image")

        if book_form.is_valid() and image_form.is_valid():
            book = book_form.save(commit=False)
            book.user = request.user

            # images = image_form.save(commit=False)
            # images.book = book
            # images.save()

            if len(images):
                for img in images:
                    img_instance = Image(book=book, image=img)
                    book.save()
                    img_instance.save()
            book.save()
            return redirect("review:index")
    else:
        book_form = bookForm()
        image_form = ImageForm()
    context = {
        "book_form": book_form,
        "image_form": image_form,
    }
    return render(request, "book/create.html", context)


def update(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    imagess = Image.objects.filter(book_id=book.pk)
    if request.method == "POST":
        book_form = bookForm(request.POST, instance=book)
        image_form = ImageForm(request.POST, request.FILES)
        images = request.FILES.getlist("image")

        for img in imagess:
            if img.image:
                img.delete()

        if book_form.is_valid() and image_form.is_valid():
            book = book_form.save(commit=False)

            if len(images):
                for image in images:
                    image_instance = Image(book=book, image=image)
                    book.save()
                    image_instance.save()
            book.save()
            return redirect("review:index")
    else:
        book_form = bookForm(instance=book)
        if imagess:
            image_form = ImageForm(instance=imagess[0])
        else:
            image_form = ImageForm()
    context = {
        "book_form": book_form,
        "image_form": image_form,
    }
    return render(request, "book/create.html", context)


def delete(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    book.delete()
    return redirect("review:index")


def book_list(request, pk):
    if pk == 1:
        genre = "공포/추리"
    elif pk == 2:
        genre = "판타지/무협"
    elif pk == 3:
        genre = "로맨스/가족"
    elif pk == 4:
        genre = "역사/철학"
    elif pk == 5:
        genre = "정치/경제"
    book_genre = Book.objects.filter(genre__contains=pk)

    context = {
        "book_genre": book_genre,
        "genre": genre,
    }

    return render(request, "book/book_list.html", context)
