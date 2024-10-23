# from django.urls import path
# from users.views import RegisterView, LoginView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ]
from django.urls import path
from .views import RegisterView, LoginView, CompanyStatusView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('company-status/<int:user_id>/', CompanyStatusView.as_view(), name='company-status'),
]
