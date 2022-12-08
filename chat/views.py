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


def index(request):
    return render(request, "chat/index.html")

    #pk는 review.pk임
def room(request, pk):
    # print(Review.pk)
    # room = Review.objects.get(pk=pk)
    room = pk
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, "chat/room.html", {'room':room,'messages':messages})

