from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/', views.delete, name="delete"),
    path('user_profile/<int:id>/', views.user_profile, name="user_profile"),
]