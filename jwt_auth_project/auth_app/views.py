# third-party packages imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

# local imports
from auth_app.renderers import CustomRenderer
from auth_app.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer
)

# method for generating tokens
def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token

    tokens = {
        'refresh_token': str(refresh),
        'access_token':  str(access)
    }
    
    return tokens

# Create your views here.
# UserRegistrationView -> User Registration
class UserRegistrationView(APIView):
    renderer_classes = [CustomRenderer]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
            tokens = get_tokens(user=user) 
            
            return Response({
                "tokens": tokens,
                "Message":"Registration Successful!"},
                status=status.HTTP_201_CREATED
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UserLoginView -> Login
class UserLoginView(APIView):
    renderer_classes = [CustomRenderer]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            tokens = get_tokens(user=user) 
            
            return Response({
                "tokens": tokens,
                "Message":"Login Successful!"},
                status=status.HTTP_201_CREATED
                )
            
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    