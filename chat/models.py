from django.db import models
from pjt.settings import AUTH_USER_MODEL


class Room(models.Model):
    send_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    receive_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="받는사람")
    count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now_add=True)
    


class Message(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.IntegerField(default=0)

    class Meta:
        ordering= ('created_at',)
    def __str__(self):
        return self.user.username

    # 최근 10 톡만 보여주기
    def last_10_messages(self):
        return Message.objects.order_by('-created_at').all()[:10]