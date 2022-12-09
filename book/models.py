from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


User = get_user_model()

#class book_genre(models.Model):
#    genre=models.CharField(max_length=10, unique=True)
    
#    def __str__(self):
#        return self.genre
    # def get_deferred_fields(self):
    #     return reverse('book/book_list.html',args=[self.genre])
    
class Book(models.Model):

    # 제목
    title = models.CharField(max_length=50)
    # 장르
    genre = models.CharField(max_length=10, unique=True)
    # 가격
    price = models.PositiveIntegerField()
    # 줄거리
    summary=models.TextField(max_length=500, blank=True)
    # 매칭수
    matching_count = models.PositiveIntegerField(blank=True) 
    # 도서 이미지
    #image = ProcessedImageField(
    #    blank=True,
    #    upload_to="book_image/",
    #    processors=[ResizeToFill(400, 400)],
    #    format="JPEG",
    #    options={"quality": 90},
    #)
    def __str__(self):
        return self.title   

# Create your models here.
class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
