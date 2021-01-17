from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TestView, TokenObtainPairWithHandleView

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # if we use the custom claim with the handle
    path('token/', TokenObtainPairWithHandleView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # TestView for auth
    path('test/', TestView.as_view(), name='test_auth')
]