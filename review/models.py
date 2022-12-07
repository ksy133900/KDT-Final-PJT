from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    genre_choice = [
        ("장르를 선택해주세요", "장르를 선택해주세요"),
        ("추리", "추리"),
        ("스릴러", "스릴러"),
        ("공포", "공포"),
        ("판타지", "판타지"),
        ("로맨스", "로맨스"),
    ]
    genre = models.CharField(
        max_length=20, choices=genre_choice, null=True, default="장르를 선택해주세요"
    )
    age = models.IntegerField(null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, default=1
    )

    # 조회수
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=80, blank=True)
    tags = TaggableManager(blank=True)
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )
    bookmark_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="bookmark_reviews"
    )

    def __str__(self):
        return self.title


class Photo(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_comments"
    )
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

class Match_review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    match_user = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
