from django.urls import path
from company.views import CompanyDetailsView

urlpatterns = [
    path('companydetails/', CompanyDetailsView.as_view(), name='companydetails'),

]


