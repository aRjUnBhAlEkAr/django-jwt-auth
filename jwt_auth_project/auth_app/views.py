# third-party packages imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# local imports
from auth_app.serializers import UserRegistrationSerializer

# Create your views here.
class UserRegistrationView(APIView):
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Message":{"Registration Successful!"}}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)