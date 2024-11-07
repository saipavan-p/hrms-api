from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import TimeSheet, EmpWorkDetails, CompanyDetails, PayCalculation
from .serializers import PayCalculationSerializer
from .serializers import TimesheetSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class TimesheetViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated] 
    def list(self, request, company_id, month):
        print(f"Received request to fetch timesheets for company ID: {company_id} and month: {month}")

        # Filter timesheets by company ID and month
        timesheets = TimeSheet.objects.filter(company_id=company_id, month=month)
        print(f"Filtered Timesheets Queryset: {timesheets}")

        if not timesheets:
            return Response(
                {"message": f"No timesheets found for company ID: {company_id} and month: {month}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TimesheetSerializer(timesheets, many=True)
        return Response({"Attendance_data": serializer.data}, status=status.HTTP_200_OK)

permission_classes = [IsAuthenticated] 
@api_view(['POST'])
def upload_timesheet(request):
    try:
        # Assuming the request data is a list of dictionaries
        data = request.data  
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
                    OT=entry['OT'],
                    allowance=entry['allowance'],
                    deductions=entry['deductions']
                )
            else:
                # Handle cases where empId is missing, you can skip or log it
                print(f"Skipping entry with missing empId: {entry}")

        return JsonResponse({"status": "success", "message": "Timesheet uploaded successfully"})
    except KeyError as e:
        return JsonResponse({"status": "error", "message": f"Missing key: {str(e)}"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

class SavePayData(APIView):
    permission_classes = [IsAuthenticated] 
    def post(self, request):
        serializer = PayCalculationSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()  # Save the data if valid
            return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .models import PayCalculation
from .serializers import PayCalculationSerializer

class PayCalculationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated] 
    @action(detail=False, methods=['get'])
    def unique_months(self, request):
        unique_months = PayCalculation.objects.values_list('month', flat=True).distinct()
        return Response(list(unique_months), status=status.HTTP_200_OK)
    
    permission_classes = [IsAuthenticated] 
    @action(detail=False, methods=['get'])
    def by_month(self, request):
        month = request.query_params.get('month')
        company_id = request.query_params.get('company_id')
        
        if month and company_id:
            queryset = PayCalculation.objects.filter(month=month, company_id=company_id)
            serializer = PayCalculationSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "Month and company_id parameters are required"},
            status=status.HTTP_400_BAD_REQUEST
        )
