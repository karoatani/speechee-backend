from django.urls import path
from .views import (
                    CustomTokenObtainPairView,
                    CustomRegistrationAPIView,
                    UserEnterNewPasswordView,
                    UserForgotPasswordView,
                    UserImportsCreateApiView
                    
                )
                    
app_name = 'accounts_api'

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='api-token'),
    path("register/", CustomRegistrationAPIView.as_view(), name="register"),
    path('forgot-password/', UserForgotPasswordView.as_view(), name="forgot-password"),
    path('forgot-password/enter-new/', UserEnterNewPasswordView.as_view(), name="forgot-password-enter-new"),
    path('import/', UserImportsCreateApiView.as_view(), name="document-import"),
    
    
]