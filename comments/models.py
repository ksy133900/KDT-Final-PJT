from django.db import models
from django.conf import settings

# Create your models here.
class Commentss(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='댓글내용')
    created = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    deleted = models.BooleanField(default=False, verbose_name='삭제여부')

    def __str__(self):
        return self.content
    
    class Meta:
        db_table = 'Comments'
        verbose_name = '리뷰 댓글'
        verbose_name_plural = '리뷰 댓글'