from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path('post_list/', views.post_list, name="post_list"),
]