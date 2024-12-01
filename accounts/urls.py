from django.urls import path
from .views import (
                    CustomTokenObtainPairView,
                    CustomRegistrationAPIView,
                    UserEnterNewPasswordView,
                    UserForgotPasswordView,
                    UserImportsCreateApiView,
                    UserImportsListApiView,
                    UserImportsRetrieveApiView,
                    UserIntegrationCreateApiView,
                    UserIntegrationRetrieveApiView,
                    UserCreationsListApiView
                    
                )
                    
app_name = 'accounts_api'

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='api-token'),
    path("register/", CustomRegistrationAPIView.as_view(), name="register"),
    path('forgot-password/', UserForgotPasswordView.as_view(), name="forgot-password"),
    path('forgot-password/enter-new/', UserEnterNewPasswordView.as_view(), name="forgot-password-enter-new"),
    path('import/', UserImportsCreateApiView.as_view(), name="document-import"),
    path('import/list/', UserImportsListApiView.as_view(), name="document-import-list"),
    path('creation/list/', UserCreationsListApiView.as_view(), name="user-creation-list"),
    
    path('import/retrieve/', UserImportsRetrieveApiView.as_view(), name="document-import-retrieve"),
    path('integration/', UserIntegrationCreateApiView.as_view(), name="user-integration"),
    path('integration/retrieve/<int:pk>/', UserIntegrationRetrieveApiView.as_view(), name="user-integration-retrieve"),
    
    
]