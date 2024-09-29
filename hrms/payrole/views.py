# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.generics import get_object_or_404
# from .models import EmployeeCompensation
# from .serializers import EmployeeCompensationSerializer

# class EmployeeCompensationView(APIView):
    
#     def get(self, request, pk=None):
#         if pk:
#             # Retrieve a specific employee compensation by its primary key
#             compensation = get_object_or_404(EmployeeCompensation, pk=pk)
#             serializer = EmployeeCompensationSerializer(compensation)
#             return Response(serializer.data)
#         else:
#             # List all compensations
#             compensations = EmployeeCompensation.objects.all()
#             serializer = EmployeeCompensationSerializer(compensations, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         # Create a new employee compensation
#         serializer = EmployeeCompensationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         # Update an existing employee compensation
#         compensation = get_object_or_404(EmployeeCompensation, pk=pk)
#         serializer = EmployeeCompensationSerializer(compensation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         # Delete an employee compensation
#         compensation = get_object_or_404(EmployeeCompensation, pk=pk)
#         compensation.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import viewsets
from .models import EmployeeCompensation
from rest_framework.response import Response
from rest_framework import status

from .serializers import EmployeeCompensationSerializer

class EmployeeCompensationViewSet(viewsets.ModelViewSet):
    queryset = EmployeeCompensation.objects.all()
    serializer_class = EmployeeCompensationSerializer

    def create(self, request, *args, **kwargs):
        company_id = request.data.get('company')
        if not company_id:
            return Response({"company": ["This field may not be null."]}, status=status.HTTP_400_BAD_REQUEST)
        
        # Handle creation
        return super().create(request, *args, **kwargs)