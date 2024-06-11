from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import user_registration, user_login, LogoutView

urlpatterns = [
    path("register/", user_registration, name="user_registration"),
    path("login/", user_login, name="user_login"),
    path("logout/", LogoutView.as_view(), name="user_logout"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]