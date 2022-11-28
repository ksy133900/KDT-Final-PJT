from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # username = models.CharField(max_length=16, unique=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    age = models.IntegerField(null=True)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    intro = models.TextField(blank=True)  # 소개글
    image = ProcessedImageField(
        blank=True,
        upload_to="profile/",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )

    def __str__(self):
        return self.user.email
