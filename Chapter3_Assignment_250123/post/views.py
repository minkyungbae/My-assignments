from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article


# index 보기
def index(request):
    return render(request, "post/index.html")


# post list 보기
def post_list(request):
    post_list = Article.objects.all().order_by("created_at")
    context = {"post_list":post_list}
    return render(request, "post/post_list.html", context)


