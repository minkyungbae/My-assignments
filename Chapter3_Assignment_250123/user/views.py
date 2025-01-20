from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods



# 회원가입
# @require_http_methods : GET, POST일 때만 작동(코드가 안전해짐)
@require_http_methods("GET", "POST")
def signup(request):
    if request.method == "POST":
        # UserCreationForm : username과 password로 새로운 user를 생성해주는 모델
        form = UserCreationForm(request.POST) # 바인딩 form : POST로 채워져서 만들어지는 form
        if form.is_valid(): # POST로 받은 값이 유효하다면,
            user = form.save()  # user에 POST 값 저장
            auth_login(request, user) # user 값으로 자동으로 로그인 하기
            return redirect("index")    # 로그인된 상태로 index로 가기
    else:
        form = UserCreationForm()   # GET일 때는 form으로 보여주기
    context = {'form': form}
    return render(request, "user/signup.html", context)


# 로그인
# @require_http_methods : GET, POST일 때만 작동(코드가 안전해짐)
@require_http_methods("GET", "POST")
def login(request):
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)    # 로그인을 위한 기본적인 form을 제공해줌
        if form.is_vaild(): # form이 POST 값으로 유효하다면,
            auth_login(request, form.get_user())    # 로그인 하기
            next_url = request.GET.get("next") or "index"   # GET 정보가 있으면 next로 가고, 없으면 index로 가자
            return redirect(next_url)   # 이전까지 실행되던 창으로 돌아가자
    else:
        form = AuthenticationForm() # GET일 경우 form만 출력
    context = {"form": form}
    return render(request, "user/login.html", context)


# 로그아웃
# @require_POST : POST일 때만 작동
@require_POST
def logout(request):
    if request.user.is_authenticated:   # user가 로그인된 상태일 때,
        auth_logout(request)    # 로그아웃 하기
    return redirect("index")


# 회원탈퇴
# @require_POST : POST일 때만 작동
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("index")
