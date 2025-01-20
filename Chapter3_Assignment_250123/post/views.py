from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# index 보기
def index(request):
    return render(request, "post/index.html")


