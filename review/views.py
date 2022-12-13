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
from django.db.models import Q
from book.models import *
from django.db.models import Q

# Create your views here.


def pro_index(request):
    auth_logout(request)
    return render(request, "review/pro_index.html")


def index(request):
    reviews = Review.objects.order_by("-pk")
    profile = Profile.objects.order_by("-pk")
    # 장르별 최고 평점 1권만 filter로 수정해야함.
    books = Book.objects.all()
    # 전체 도서 평점 top10[10개까지]
    book_top10 = Book.objects.all()[:10]
    # 장르별 최근 리뷰 도서[3개까지]
    new_book = Book.objects.order_by("-pk")[:3]
    book_image = Image.objects.all()

    context = {
        "reviews": reviews,
        "profile": profile,
        "books": books,
        "book_image": book_image,
        "new_book": new_book,
        "book_top10": book_top10,
    }
    return render(request, "review/index.html", context)


def faq(request):
    return render(request, "review/faq.html")


def matching(request):
    user = User.objects.order_by("-pk")
    user_address = User.objects.values_list("address")
    profile = Profile.objects.order_by("-pk")
    notes_notice = len(Notes.objects.filter(to_user_id=request.user.pk, read=0))

    context = {
        "profile": profile,
        "notes_notice": notes_notice,
        "user": user,
    }
    print(user_address)
    return render(request, "review/matching.html", context)


def search(request):
    search_keyword = request.GET.get("search", "")
    search_option = request.GET.get(
        "search_option", ""
    )  # title, title_content, hashtag, user
    # reviews = Review.objects.order_by("-pk")
    profiles = Profile.objects.order_by("-pk")

    if search_keyword:
        if search_option == "user":
            # ForeignKey icontains
            # {Review의 User field}__{User의 nickname field}__icontains
            search_profiles = profiles.filter(Q(nickname__icontains=search_keyword))
    # if search_keyword:
    #     if search_option == "title":
    #         search_reviews = reviews.filter(title__icontains=search_keyword)

    #     elif search_option == "title_content":
    #         # Q: ORM WHERE에서 or 연산을 수행
    #         search_reviews = reviews.filter(
    #             Q(title__icontains=search_keyword)
    #             | Q(content__icontains=search_keyword)
    #         )
    #     elif search_option == "hashtag":
    #         # distinct(): 중복 제거
    #         # 만약 해시태그가 #1, #11, #111인 글이 하나 있고, 1을 검색하면
    #         # 같은 글이 3개가 보여짐.
    #         search_reviews = reviews.filter(
    #             tags__name__icontains=search_keyword
    #         ).distinct()
    #     elif search_option == "user":
    #         # ForeignKey icontains
    #         # {Review의 User field}__{User의 nickname field}__icontains
    #         search_profiles = profiles.filter(Q(nickname__icontains=search_keyword))

    context = {
        # "search_reviews": search_reviews,
        "search_profiles": search_profiles,
    }

    return render(request, "review/search.html", context)


@login_required
def create(request, book_pk):

    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        # photo_form = PhotoForm(request.POST, request.FILES)
        book = Book.objects.get(pk=book_pk)
        book_images = Image.objects.filter(
            book__id=book_pk
        )  # book_pk로 Image.book_id가 필터(없어도 필터라 쿼리셋으로 변수지정)

        tags = request.POST.get("tags", "").split(",")

        # if request.POST.get("tags", "") != "":
        #     tags = request.POST.get("tags", "").split(",")
        # else:
        #     tags = None

        if review_form.is_valid():  # and photo_form.is_valid():
            review = review_form.save(commit=False)
            # photo = photo_form.save()
            review.user = request.user
            review.book = book

            # 지정된 변수가 없으면 review.book_image는 지정이 안되어 null처리됨
            if book_images:
                # 변수가 있다면 for문으로 셋을 풀고 review.book_image에 지정
                for book_image in book_images:
                    review.book_image = book_image
            review.save()
            if tags:
                for tag in tags:
                    tag = tag.strip()
                    review.tags.add(tag)
                    review.save()
                return redirect("review:index")
    else:
        review_form = ReviewForm()

    context = {
        "review_form": review_form,
    }
    return render(request, "review/create.html", context)


# 글 수정 시작
@login_required
def update(request, pk, book_pk):
    review = Review.objects.get(pk=pk)  # 수정하기 위해서 이전 글을 불러와야 하므로
    if request.method == "POST":
        # POST : input 값 가져와서 검증하고 DB에 저장
        # 기존에 있는 값을 수정하므로 그 기존값을 받아와야 한다. 없으면 수정이 아니라 글을 생성함
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        # photo_form = PhotoForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():  # and photo_form.is_valid():
            review_form.save()
            # photo_form.save()
            # 유효성 검사 통과하면 상세보기 페이지로
            return redirect("review:detail", book_pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : forms을 제공
        review_form = ReviewForm(instance=review)
        # photo_form = PhotoForm(instance=review)
    context = {
        "review_form": review_form,
        # "photo_form": photo_form,
    }
    return render(request, "review/create.html", context)


# 글 수정 끝

# 글 삭제 시작
def delete(request, pk, book_pk):
    Review.objects.get(id=pk).delete()
    return redirect("review:detail", book_pk)


# 글 삭제 끝


def detail(request, book_pk):
    reviews = Review.objects.filter(book_id=book_pk).order_by("-pk")
    book = Book.objects.get(pk=book_pk)
    book_image = Image.objects.get(book_id=book_pk)
    genre_list = ["공포/추리", "판타지", "로맨스/가족", "역사/철학", "정치/경제"]
    genre = genre_list[int(book.genre) - 1]

    context = {
        "reviews": reviews,
        "book": book,
        "book_image": book_image,
        "genre": genre,
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
        "likeCount": review.like_users.count(),
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

def search(request):
    search_keyword = request.GET.get("search", "")
    search_option = request.GET.get(
        "search_option", ""
    )  # title, title_content, hashtag, user
    # reviews = Review.objects.order_by("-pk")
    profiles = Profile.objects.order_by("-pk")

    if search_keyword:
        if search_option == "nickname":
            search_profiles = profiles.filter(Q(nickname__icontains=search_keyword))

        elif search_option == "genre":
            # Q: ORM WHERE에서 or 연산을 수행
            search_profiles = profiles.filter(Q(genre__icontains=search_keyword))

        elif search_option == "location":
            search_profiles = profiles.filter(Q(location__icontains=search_keyword))

        elif search_option == "ages":
            search_profiles = profiles.filter(Q(ages__icontains=search_keyword))

    context = {
        # "search_reviews": search_reviews,
        "search_profiles": search_profiles,
    }

    return render(request, "review/search.html", context)
