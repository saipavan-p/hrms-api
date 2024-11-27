

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimesheetViewSet, upload_timesheet, SavePayData, PayCalculationViewSet
from . import views

router = DefaultRouter()
router.register(r'timesheets', TimesheetViewSet, basename='timesheets')

urlpatterns = [
    path('', include(router.urls)),
    # path('upload_timesheet/', upload_timesheet, name='upload_timesheet'),
    path('save-pay-data/', SavePayData.as_view(), name='save-pay-data'),
    path('paycalculation/unique-months/', PayCalculationViewSet.as_view({'get': 'unique_months'}), name='unique-months'),
    path('paycalculation/by-month/', PayCalculationViewSet.as_view({'get': 'by_month'}), name='paycalculation-by-month'),
    path('upload-attendance/', views.upload_attendance_file, name='upload_attendance_file'),

]
