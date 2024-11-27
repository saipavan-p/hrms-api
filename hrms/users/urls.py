
from django.urls import path
from .views import RegisterView, LoginView, CompanyStatusView
from rest_framework_simplejwt.views import TokenRefreshView,     TokenObtainPairView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('company-status/<int:user_id>/', CompanyStatusView.as_view(), name='company-status'),
]
