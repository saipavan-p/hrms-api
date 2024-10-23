from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import TimeSheet, EmpWorkDetails, CompanyDetails
from .serializers import TimesheetSerializer
from rest_framework import viewsets


@api_view(['POST'])
def upload_timesheet(request):
    try:
        # Assuming the request data is a list of dictionaries
        data = request.data  # The list of timesheet entries directly
        for entry in data:
            # Check if empId exists in the entry, and handle the case where it's missing or empty
            empId = entry.get('empId', None)
            company_id = entry.get('company')
            if empId and company_id:
                # Fetch the employee object
                employee = EmpWorkDetails.objects.get(empId=empId)
                
                # Fetch the company object using company_id
                company = CompanyDetails.objects.get(companyId=company_id)

                # Create the TimeSheet entry
                TimeSheet.objects.create(
                    empId=employee,
                    company=company,
                    name=entry['name'],
                    month=entry['month'],
                    no_of_days=entry['noOfDays'],
                    attendance=entry['attendance'],
                    lop_days=entry['lopDays']
                )
            else:
                # Handle cases where empId is missing, you can skip or log it
                print(f"Skipping entry with missing empId: {entry}")

        return JsonResponse({"status": "success", "message": "Timesheet uploaded successfully"})
    except KeyError as e:
        return JsonResponse({"status": "error", "message": f"Missing key: {str(e)}"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    


class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = TimeSheet.objects.all()
    serializer_class = TimesheetSerializer

