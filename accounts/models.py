from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


# Create your models here.
class User(AbstractUser):

    matching = models.BooleanField(default=True)  # 모집 여부
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    notice_note = models.BooleanField(default=True)
    note_notice = models.BooleanField(default=True)  # 메일 여부
    # address = models.CharField(max_length=50, null=True)


class Profile(models.Model):
    nickname = models.CharField(max_length=8, unique=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # genre = models.OneToOneField(User, related_name="genre", on_delete=models.CASCADE)
    intro = models.TextField(null=True, blank=True)  # 소개글
    image = ProcessedImageField(
        blank=True,
        upload_to="profile/",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    age = models.CharField(max_length=20, null=True, blank=True)  # 나이
    genre_choice = [
        ("장르", "장르"),
        ("추리", "추리"),
        ("스릴러", "스릴러"),
        ("공포", "공포"),
        ("판타지", "판타지"),
        ("로맨스", "로맨스"),
    ]
    genre = models.CharField(
        blank=True, max_length=20, default="장르", choices=genre_choice
    )  # 선호 장르
    days = [
        ("요일", "요일"),
        ("월", "월요일"),
        ("화", "화요일"),
        ("수", "수요일"),
        ("목", "목요일"),
        ("금", "금요일"),
        ("토", "토요일"),
        ("일", "일요일"),
    ]
    day = models.CharField(blank=True, max_length=20, choices=days, default="요일")
    times = [
        ("시간", "시간"),
        ("오전", "오전 : 06:00 ~ 11:59 사이"),
        ("오후", "오후 : 12:00 ~ 17:59 사이"),
        ("저녁", "저녁 : 18:00 ~ 23:59 사이"),
    ]
    time = models.CharField(
        blank=True, max_length=20, choices=times, default="시간"
    )  # 선호 시간
    age_select = [
        ("선택해주세요", "선택해주세요"),
        ("20대", "20대"),
        ("30대", "30대"),
        ("40대", "40대"),
        ("50대", "50대"),
    ]
    ages = models.CharField(
        blank=True, max_length=20, default="선택해주세요", choices=age_select
    )  # 선호 장르
    location = models.CharField(blank=True, max_length=20, null=True)
    # 선호시간
    daytime = models.TextField(blank=True)

    def __str__(self):
        return self.user.email
