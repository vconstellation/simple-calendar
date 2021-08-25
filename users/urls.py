from django.urls import path
from django.contrib.auth.urls import views as auth_views
from .views import register_user

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register'),
]