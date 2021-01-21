from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
# for the custom claim, if I wanted it
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer

class TestView(APIView):
    # we can take this out if we put DEFAULT_PERMISSION_CLASSES to include this in settings
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'Message': 'You are authenticated!'}
        return Response(content)

class TokenObtainPairWithHandleView(TokenObtainPairView):
    permission_classes = (AllowAny,) # only need this if DEFAULT_PER... is somethign like isAuthenticated
    serializer_class = CustomTokenObtainPairSerializer

class UserCreate(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer