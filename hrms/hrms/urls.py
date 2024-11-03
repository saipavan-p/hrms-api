# # from django.contrib import admin
# # from django.urls import path, include
# # from django.conf import settings
# # from django.conf.urls.static import static

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('api/', include('users.urls')), 
# #     path('api/', include('company.urls')), 
# #     # path('api/', include('employee.urls')),  
 
 

# # ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from employee.views import CombinedDetailsViewSet

# # Create a router and register our viewsets with it.
# router = DefaultRouter()

# # Register the CombinedDetailsViewSet with the router
# # You can name it as appropriate for your app (e.g., employee-details)
# router.register(r'employee', CombinedDetailsViewSet, basename='employee-details')

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from employee.views import CombinedDetailsViewSet
from payrole.views import EmployeeCompensationViewSet,PayrollSettingsView
from timesheet.views import upload_timesheet, TimesheetViewSet


# Create a router and register the employee viewset
router = DefaultRouter()
router.register(r'employee', CombinedDetailsViewSet, basename='employee-details')
router.register(r'payroledetails', EmployeeCompensationViewSet, basename='employee-compensation')

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin URLs
#     path('api/', include('users.urls')),  # Include users app URLs
#     path('api/', include('company.urls')),  # Include company app URLs
#     # path('api/',include('payrole.urls')), #Include company app URLs
#     path('', include(router.urls)),  # Include employee viewset URLs from the router
#     # path('api/', include(router.urls)),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin URLs
#     path('api/', include('users.urls')),  # Include users app URLs
#     path('api/', include('company.urls')),  # Include company app URLs
#     path('', include(router.urls)),  # Include employee viewset URLs from the router
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URLs
    path('api/', include('users.urls')),  # Include users app URLs
    path('api/', include('company.urls')),  # Include company app URLs
    path('api/', include(router.urls)),  # <== This includes the 'payroledetails' and 'employee' routes under /api/
    path('timesheet/upload/', upload_timesheet, name='upload_timesheet'),
    path('payroll-settings/<int:company_id>/', PayrollSettingsView.as_view(), name='payroll-settings'),
    # path('timesheet-view/<int:company_id>/', TimesheetViewSet.as_view({'get': 'list'}), name='TimesheetViewSet'),
    # path('timesheet-view/<int:company_id>/', TimesheetViewSet.as_view({'get': 'list'}), name='timesheet-view'),
    # path('timesheet-view/<int:company_id>/', TimesheetViewSet.as_view({'get': 'list'}), name='timesheet-view'),
    path('timesheet-view/<int:company_id>/<str:month>/', TimesheetViewSet.as_view({'get': 'list'}), name='timesheet-view'),
    path('api/', include('timesheet.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

