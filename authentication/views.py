from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# for the custom claim, if I wanted it
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'Message': 'You are authenticated!'}
        return Response(content)

class TokenObtainPairWithHandleView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer