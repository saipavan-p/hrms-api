from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import TimeSheet, EmpWorkDetails, CompanyDetails
from .serializers import TimesheetSerializer
from rest_framework import viewsets

# class TimesheetViewSet(viewsets.ModelViewSet):
#     serializer_class = TimesheetSerializer

#     def get_queryset(self):
#         # Get the company ID from the query parameters
#         company_id = self.request.query_params.get('company_id')

#         if company_id:
#             # Filter timesheets by the provided company ID
#             return TimeSheet.objects.filter(company=company_id)
        
#         # If no company ID is provided, return an empty queryset
#         return TimeSheet.objects.none()
    # def get_queryset(self):
    #     company_id = self.request.query_params.get('company_id')
    #     if not company_id:
    #         return TimeSheet.objects.none()
    #     return TimeSheet.objects.filter(company=company_id)

# class TimesheetViewSet(APIView):
    
#     def get(self,company_id):
#         try:
#             company_id = CompanyDetails.objects.get(companyId=company_id)
#             print(f"Filtering Timesheets for Company ID: {company_id}")  # Debug log
        
            # # If company_id is provided, filter the TimeSheet records by company
            # if company_id is not None:
            #     try:
            #         # Ensure company_id is converted to an integer if it's a valid number
            #         company_id = int(company_id)
            #         return TimeSheet.objects.filter(company=company_id)  # Correct filtering here
            #     except ValueError:
            #         print(f"Invalid company_id provided: {company_id}")
            #         return TimeSheet.objects.none()
            

            # # If no company_id is provided, return an empty queryset
            # return TimeSheet.objects.none()
        #     TimeSheetdata = TimeSheet.objects.filter(company_id=company_id)
        #     if not TimeSheetdata:
        #             return Response({"error": "No payroll settings found for this company."}, status=status.HTTP_404_NOT_FOUND)
            
        #     serializer_class = TimesheetSerializer(TimeSheetdata)
        #     return Response(serializer_class.data, status=status.HTTP_200_OK)
        
        # except TimeSheet.DoesNotExist:
        #     return Response({"error": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

# class TimesheetViewSet(viewsets.ModelViewSet):
#     serializer_class = TimesheetSerializer

#     def get_queryset(self):
#         # Get the 'company_id' from the URL kwargs
#         company_id = self.kwargs.get('company_id')
#         print(f"Filtering timesheets for company ID: {company_id}")  # Debug log

#         # Ensure we correctly filter by the company foreign key
#         if company_id:
#             queryset = TimeSheet.objects.filter(company=company_id)
#             print(f"Filtered queryset : {queryset}")  # Debug log to verify filtering
#             return queryset
        
#         return TimeSheet.objects.none()  # Return empty if no company_id provided

class TimesheetViewSet(viewsets.ViewSet):
    def list(self, request, company_id):
        print(f"Received request to fetch timesheets for company ID: {company_id}")

        # Filter timesheets by company ID
        timesheets = TimeSheet.objects.filter(company_id=company_id)
        print(f"Filtered Timesheets Queryset: {timesheets}")

        if not timesheets:
            return Response(
                {"message": f"No timesheets found for company ID: {company_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TimesheetSerializer(timesheets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                    lop_days=entry['lopDays'],
                    OT=entry['OT']
                )
            else:
                # Handle cases where empId is missing, you can skip or log it
                print(f"Skipping entry with missing empId: {entry}")

        return JsonResponse({"status": "success", "message": "Timesheet uploaded successfully"})
    except KeyError as e:
        return JsonResponse({"status": "error", "message": f"Missing key: {str(e)}"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    


# class TimesheetViewSet(viewsets.ModelViewSet):
#     queryset = TimeSheet.objects.all()
#     serializer_class = TimesheetSerializer

