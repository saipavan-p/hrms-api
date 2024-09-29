from django.urls import path
from .views import CompanyDetailsView

urlpatterns = [
    path('companydetails/', CompanyDetailsView.as_view(), name='companydetails'),

]


