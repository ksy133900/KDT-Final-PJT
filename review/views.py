from django.shortcuts import render, redirect
from .models import *
from .forms import *
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.


def pro_index(request):
    return render(request, "review/pro_index.html")


def index(request):
    reviews = Review.objects.order_by("-pk")

    profile = Profile.objects.order_by("-pk")
    context = {
        "reviews": reviews,
        "profile": profile,
    }

    return render(request, "review/index.html", context)


def matching(request):

    return render(request, "review/matching.html")


def genre(request):
    test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    context = {"test": test}
    return render(request, "review/genre.html", context)


@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        photo_form = PhotoForm(request.POST, request.FILES)
        images = request.FILES.getlist("image")
        tags = request.POST.get("tags", "").split(",")

        if request.POST.get("tags", "") != "":
            tags = request.POST.get("tags", "").split(",")
        else:
            tags = None

        if review_form.is_valid() and photo_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user

            if len(images):
                for image in images:
                    image_instance = Photo(review=review, image=image)
                    review.save()
                    image_instance.save()

            review.save()
            if tags:
                for tag in tags:
                    tag = tag.strip()
                    review.tags.add(tag)
                    review.save()

            return redirect("review:index")
    else:
        review_form = ReviewForm()
        photo_form = PhotoForm()
    context = {
        "review_form": review_form,
        "photo_form": photo_form,
    }
    return render(request, "review/create.html", context)


def detail(request):
    reviews = Review.objects.order_by("-pk")

    context = {
        "reviews": reviews
    }
    return render(request, "review/detail.html", context)

# 리뷰카드 좋아/싫어
def like_users(request,):
    print("====>>>>>>", request)
    review = Review.objects.get(pk=4)
    print("====>>>>>>", review.id)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        existed_user = False
    else:
        review.like_users.add(request.user)
        existed_user = True
    likeCount = review.like_users.count()

    context = {
        "existed_user": existed_user,
        "likeCount": likeCount,
    }

    return JsonResponse(context)