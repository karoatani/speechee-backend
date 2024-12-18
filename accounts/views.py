import random
from django.shortcuts import render
from .models import Account, UserImports, UserIntegration
from .serializers import CustomTokenObtainPairSerializer, CustomRegistrationSerializer, ForgotPasswordSerializer,EnterNewPasswordSerializer, UserImportsSerializer, UserIntegrationSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomRegistrationAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = CustomRegistrationSerializer
    permission_classes = (permissions.AllowAny,)
    
    

class UserForgotPasswordView(APIView):
    queryset = Account.objects.all()
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(**{'data': request.data})
        serializer.is_valid()
        entered_email = serializer.data['email']
        
        if Account.objects.filter(email=entered_email).exists():
            user_account_id = Account.objects.get(email=entered_email)
            account_id = user_account_id.id
            _forgot_password_code = random.randint(000000,999999)
            Account.objects.filter(email=entered_email).update(forgot_password_code=_forgot_password_code)

            # Send password reset token to user
            # send_password_reset_token_to_user(account_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Email not found"}, status=status.HTTP_404_NOT_FOUND)


class UserEnterNewPasswordView(APIView):
    queryset = Account.objects.all()
    serializer_class = EnterNewPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(**{'data': request.data})
        serializer.is_valid()

        data = request.data
        entered_forgot_password_code = serializer.data['forgot_password_code']
        entered_password = serializer.data['password']
        user = Account.objects.get(forgot_password_code=entered_forgot_password_code)

        if Account.objects.filter(forgot_password_code=entered_forgot_password_code).exists():
            if user:
                user.set_password(entered_password)
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        
        
        


class UserImportsCreateApiView(generics.CreateAPIView):
    queryset = UserImports.objects.all()
    serializer_class = UserImportsSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserImportsListApiView(generics.ListAPIView):
    queryset = UserImports.objects.all()
    serializer_class = UserImportsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        return super().get_queryset().filter(user=user, is_file=True)



class UserCreationsListApiView(generics.ListAPIView):
    queryset = UserImports.objects.all()
    serializer_class = UserImportsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter( is_file=False, user=user)


class UserImportsRetrieveApiView(generics.RetrieveAPIView):
    queryset = UserImports.objects.filter(is_file=True)
    serializer_class = UserImportsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset(user=user)

class UserImportsDeleteApiView(generics.UpdateAPIView):
    queryset = UserImports.objects.all()
    serializer_class = UserImportsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    

class UserIntegrationCreateApiView(generics.CreateAPIView):
    queryset = UserIntegration.objects.all()
    serializer_class = UserIntegrationSerializer
    

class UserIntegrationRetrieveApiView(generics.RetrieveAPIView):
    queryset = UserIntegration.objects.all()
    serializer_class = UserIntegrationSerializer
    
    
    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        instance = self.queryset.get(user=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
