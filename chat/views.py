from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from accounts.models import Notification
from review.models import Review
from django.db.models import Q
import json
from django.db.models.signals import post_save
from .models import Message
from django.http import JsonResponse
from datetime import datetime
from accounts.models import User


def index(request):
    return render(request, "chat/index.html")

    #pk는 review.pk임
def room(request, pk):
    print(type(pk))
    # print(Review.pk)
    # room = Review.objects.get(pk=pk)
    print(request.GET)
    room = pk
    messages = Message.objects.filter(room=room).order_by('created_at').all()
    print(messages,'111111111111111')
    # room = message['room']
    # created_at = message['created_at']
    # messages = message['content']
    print(messages[0].created_at,'7777777777777777777777777')
    message_time = messages[0]
    accounts_names=list(User.objects.filter(username=request.user).values())
    print(accounts_names[0]['username'],'33333')
    accounts_name=accounts_names[0]
    # context = {
    #     'room': room,
    #     'messages': messages,
    #     'created_at': created_at,
    #     'accounts_name':accounts_name,
    # }
    print(request.user.is_authenticated,'11111111111')
    return render(request, "chat/room.html", {'messages':messages, 'room':room, 'accounts_name':accounts_name, 'message_time':message_time})

