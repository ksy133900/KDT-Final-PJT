from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from .models import Commentss
from review.models import Review
from accounts.models import Profile
from django.http import HttpResponse

# Create your views here.
#댓글 쓰기
@login_required
def comments_write(request, pk):      #review 게시글의 pk값을 받아서 그 글에서만 댓글 쓰게끔 하려고
    user = request.POST.get('user')
    content = request.POST.get('content')
    if content:
        comment = Commentss.objects.create(content=content, user=request.user)
        comment.save()
        data = {
            'user': user,
            'content': content,
            'created_at':'방금 전',
            'comment_id':comment.id
        }
        if request.user == Review.user:
            data['self_comment']='(글쓴이)'
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

#댓글 삭제
@login_required
def comments_delete(request, pk):
    comment_id = request.POST.get('comment_id')
    target_comment = Commentss.objects.get(pk = comment_id)

    if request.user == target_comment.user:
        target_comment.deleted = True
        target_comment.save()
        data = {
            'comment_id': comment_id,
        }
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

@login_required        
def comments(request, pk):
    reviews = Review.objects.filter(pk=pk)
    context ={
        'reviews':reviews,
    }
    return render(request, "comments/comments.html",context)