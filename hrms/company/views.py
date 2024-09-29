# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import CompanyDetails
# from .serializers import CompanyDetailsSerializer

# class CompanyDetailsView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CompanyDetailsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Successfully submitted"}, status=status.HTTP_201_CREATED)
#         print(serializer.errors)  
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CompanyDetails
from .serializers import CompanyDetailsSerializer

class CompanyDetailsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CompanyDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new company instance
            company = serializer.save()
            
            # Return response with companyId
            return Response({
                "message": "Successfully submitted",
                "companyId": company.companyId  # Include companyId in the response
            }, status=status.HTTP_201_CREATED)
        
        # If validation fails, print errors and return bad request
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
