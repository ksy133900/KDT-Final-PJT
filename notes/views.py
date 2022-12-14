from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.


@login_required
def index(request):
    # notes = request.user.user_to.order_by("-created_at")
    notes = Notes.objects.filter(to_user_id=request.user.id).order_by("-created_at")
    context = {
        "notes": notes,
    }
    return render(request, "notes/index.html", context)


@login_required
def sent(request):
    # to_notes = request.user.user_from.order_by("-created_at")
    to_notes = Notes.objects.filter(from_user_id=request.user.id).order_by(
        "-created_at"
    )
    context = {
        "to_notes": to_notes,
    }
    return render(request, "notes/index.html", context)


@login_required
def mail(request):
    form = NotesForm(request.POST or None)
    if form.is_valid():
        to_id = get_user_model().objects.filter(username=request.POST["to_id"])
        for id in to_id:
            temp = form.save(commit=False)
            temp.to_user = id
            temp.from_user = request.user
            temp.save()
        return redirect("notes:index")
    context = {
        "form": form,
    }
    return render(request, "notes/mail.html", context)


@login_required
def detail(request, pk):

    note = get_object_or_404(Notes, pk=pk)
    if request.user == note.to_user:
        if not note.read:
            note.read = True
            note.save()
        if not request.user.user_to.filter(read=False).exists():
            request.user.notice_note = True
            request.user.save()
        return render(request, "notes/detail.html", {"note": note})
    elif request.user == note.from_user:
        return render(request, "notes/detail.html", {"note": note})
    else:
        return redirect("notes:index")


@login_required
def delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect("notes:index")
