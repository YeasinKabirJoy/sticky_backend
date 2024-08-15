from django.urls import path
from .views import SignUp,Login,Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('signup/',SignUp.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    path('token/verify/',TokenVerifyView.as_view(),name='token-verify'),
]
