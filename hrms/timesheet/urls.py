# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TimesheetViewSet, upload_timesheet

# router = DefaultRouter()
# router.register(r'timesheets', TimesheetViewSet)
# router.register(r'timesheets', TimesheetViewSet, basename='timesheets')  # Add basename for clarity

# urlpatterns = [
#     path('', include(router.urls)),
#     path('upload_timesheet/', upload_timesheet, name='upload_timesheet'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimesheetViewSet, upload_timesheet, SavePayData, PayCalculationViewSet

router = DefaultRouter()
router.register(r'timesheets', TimesheetViewSet, basename='timesheets')

urlpatterns = [
    path('', include(router.urls)),
    # path('upload_timesheet/', upload_timesheet, name='upload_timesheet'),
    path('save-pay-data/', SavePayData.as_view(), name='save-pay-data'),
    path('paycalculation/unique-months/', PayCalculationViewSet.as_view({'get': 'unique_months'}), name='unique-months'),
    path('paycalculation/by-month/', PayCalculationViewSet.as_view({'get': 'by_month'}), name='paycalculation-by-month'),
]
