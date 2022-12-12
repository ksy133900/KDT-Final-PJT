from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.pro_index, name="pro_index"),
    path("index/", views.index, name="index"),
    # 도서 리뷰 작성
    path("create/<int:book_pk>", views.create, name="create"),
    # 도서 디테일 화면 - 도서정보 + 리뷰목록
    path("detail/<int:book_pk>", views.detail, name="detail"),
    # 유저목록 - 매칭가능 유저들의 목록
    path("matching/", views.matching, name="matching"),
    # 글 수정
    path("update/<int:pk>,<int:book_pk>", views.update, name="update"),
    # 글 삭제
    path("delete/<int:pk>,<int:book_pk>", views.delete, name="delete"),
    # 리뷰카드 좋아/싫어 버튼
    path("detail/<int:book_pk>/like/<int:review_pk>", views.like, name="like"),
    # FAQ
    path("faq/", views.faq, name="faq"),
    # 도서 리뷰 작성
    path("match_create/", views.match_create, name="match_create"),
    # 매칭후기 게시판
    path("match_board/", views.match_board, name="match_board"),
    # 검색 페이지
    path("search/", views.search, name="search"),
]
