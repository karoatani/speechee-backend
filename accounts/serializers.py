import random
import string
from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Account, UserImports, UserIntegration
from accounts.parsers.parser_factory import ParserFactory

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["access"] = str(refresh.access_token)
        data["email"] = self.user.email
        data['user'] = self.user.id

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token
    
    
class CustomRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ("id", "email","password")

        extra_kwargs = {
            "email": {
                "validators": [
                    EmailValidator,
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="This email already exist, use a unique email address",
                    ),
                ]
            }
        }
        
    def create(self, validated_data):
        email = validated_data["email"]
        users_alphabets = "".join(random.choices(string.ascii_lowercase, k=5))
        users_number = random.randint(00000, 99999)
        username = str(users_alphabets) + str(users_number)
        
        user = Account.objects.create(
            username=username,
            email=email,
            is_active=True,
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

    
    

class ForgotPasswordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['email',]

class EnterNewPasswordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['forgot_password_code', 'password']



class UserImportsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserImports
        fields = ["id", "user", "title", "content","content2" ,"file", "is_file","is_deleted", "date_created", "last_updated"]
        
        
    def create(self, validated_data):
        instance = super().create(validated_data)
        if not instance.is_file:
            return instance
        file_path = instance.file.path
        parser = ParserFactory.get_parser(file_path=file_path)
        title, content = parser.parse(file_path=file_path)
        instance.title = " ".join(title)
        instance.content = " ".join(content)
        instance.save()
        return instance 
        
        
class UserIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIntegration
        fields = ['id', 'user', 'app_name', 'token', 'pub_id']