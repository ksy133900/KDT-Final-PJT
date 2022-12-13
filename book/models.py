from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):

    # 제목
    title = models.CharField(max_length=50)
    # 장르
    genre_choice = [
        ("1", "공포/추리"),
        ("2", "판타지"),
        ("3", "로맨스/가족"),
        ("4", "역사/철학"),
        ("5", "정치/경제"),
    ]
    genre = models.CharField(blank=True, max_length=20, choices=genre_choice, null=True)
    # 가격
    price = models.PositiveIntegerField()
    # 줄거리
    summary = models.TextField(max_length=500, blank=True)
    # 매칭수
    matching_count = models.PositiveIntegerField(default=0, blank=True)
    # 평점
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, default=1)

    def __str__(self):
        return self.title


# 도서 이미지
class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    image = ProcessedImageField(
        upload_to="images/",
        null=True,
        processors=[ResizeToFill(450, 450)],
        options={"quality": 60},
        format="JPEG",
    )
