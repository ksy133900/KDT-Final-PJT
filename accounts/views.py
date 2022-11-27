from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):

    if request.user.is_authenticated:
        return redirect("review:index")
    # 로그인 상태면 회원가입 ㄴㄴ
    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()

            return redirect("review:index")
    else:
        signup_form = CustomUserCreationForm()

    context = {
        "signup_form": signup_form,
    }

    return render(request, "accounts/signup.html", context)


def login(request):
    # 로그인 상태면 로그인 ㄴㄴ
    if request.user.is_authenticated:
        return redirect("review:index")

    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get("next") or "review:index")
    else:
        login_form = AuthenticationForm()

    context = {
        "login_form": login_form,
    }

    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("review:index")
