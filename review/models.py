from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.core.validators import MinValueValidator, MaxValueValidator
from book.models import *

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    age = models.IntegerField(null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, default=1
    )

    # 조회수
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    book_image = models.ForeignKey(
        Image, on_delete=models.CASCADE, blank=True, null=True
    )


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
