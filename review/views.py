from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from notes.models import Notes
from accounts.models import Profile
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Count
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as auth_logout
from accounts.models import *
from book.models import *

# Create your views here.


def pro_index(request):
    auth_logout(request)
    return render(request, "review/pro_index.html")


def index(request):
    reviews = Review.objects.order_by("-pk")
    profile = Profile.objects.order_by("-pk")
    books = Book.objects.all()

    context = {
        "reviews": reviews,
        "profile": profile,
        "books": books,
    }
    return render(request, "review/index.html", context)


def faq(request):
    return render(request, "review/faq.html")


def matching(request):
    user = User.objects.order_by("-pk")
    user_address = User.objects.values_list("address")
    # address_split = user.address.split(" ")
    # address1 = address_split[0]
    # address2 = address_split[1]
    profile = Profile.objects.order_by("-pk")
    notes_notice = len(Notes.objects.filter(to_user_id=request.user.pk, read=0))
    context = {
        "profile": profile,
        "notes_notice": notes_notice,
        "user": user,
        # "address1": address1,
        # "address2": address2,
    }
    print(user_address)
    return render(request, "review/matching.html", context)


@login_required
def create(request, book_pk):

    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        photo_form = PhotoForm(request.POST, request.FILES)
        book = Book.objects.get(pk=book_pk)

        images = request.FILES.getlist("image")
        tags = request.POST.get("tags", "").split(",")

        # if request.POST.get("tags", "") != "":
        #     tags = request.POST.get("tags", "").split(",")
        # else:
        #     tags = None

        if review_form.is_valid() and photo_form.is_valid():
            review = review_form.save(commit=False)
            photo = photo_form.save()
            review.user = request.user
            review.book = book

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


# 글 수정 시작
@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)  # 수정하기 위해서 이전 글을 불러와야 하므로
    if request.method == "POST":
        # POST : input 값 가져와서 검증하고 DB에 저장
        # 기존에 있는 값을 수정하므로 그 기존값을 받아와야 한다. 없으면 수정이 아니라 글을 생성함
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        photo_form = PhotoForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid() and photo_form.is_valid():
            review_form.save()
            photo_form.save()
            # 유효성 검사 통과하면 상세보기 페이지로
            return redirect("review:detail")
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : forms을 제공
        review_form = ReviewForm(instance=review)
        photo_form = PhotoForm(instance=review)
    context = {
        "review_form": review_form,
        "photo_form": photo_form,
    }
    return render(request, "review/create.html", context)


# 글 수정 끝

# 글 삭제 시작
def delete(request, book_pk):
    Review.objects.get(id=book_pk).delete()
    return redirect("review:detail")


# 글 삭제 끝


def detail(request, book_pk):
    reviews = Review.objects.filter(book_id=book_pk).order_by("-pk")
    book = Book.objects.get(pk=book_pk)

    context = {
        "reviews": reviews,
        "book": book,
    }
    return render(request, "review/detail.html", context)


# 리뷰카드 좋아/싫어
# def like_users(
#     request,
# ):
#     print("====>>>>>>", request)
#     review = Review.objects.get(pk=4)
#     print("====>>>>>>", review.id)
#     if request.user in review.like_users.all():
#         review.like_users.remove(request.user)
#         existed_user = False
#     else:
#         review.like_users.add(request.user)
#         existed_user = True
#     likeCount = review.like_users.count()

#     context = {
#         "existed_user": existed_user,
#         "likeCount": likeCount,
#     }

#     return JsonResponse(context)


def like(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    book = Book.objects.get(pk=book_pk)

    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True

    data = {
        "isLiked": is_liked,
    }

    return JsonResponse(data)


def match_board(request):
    test = Match_review.objects.all()
    context = {
        "test": test,
    }
    return render(request, "review/match_board.html", context)


def match_create(request):
    if request.method == "POST":
        match_review_form = Match_reviewForm(request.POST)
        if match_review_form.is_valid():
            match_review = match_review_form.save(commit=False)
            match_review.user = request.user
            match_review.save()
            return redirect("review:match_board")
    else:
        match_review_form = Match_reviewForm()

    context = {
        "match_review_form": match_review_form,
    }
    return render(request, "review/match_create.html", context)
