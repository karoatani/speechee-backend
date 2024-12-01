from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    forgot_password_code = models.CharField(max_length=40, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = CustomAccountManager()
    
    
def validate_file_extension(value):
    valid_extensions = ['rtf', 'docx', 'doc','md', 'txt']
    extension = value.name.split('.')[-1].lower()
    if extension not in valid_extensions:
        raise ValidationError(f"Unsupported file extension. Allowed extensions are: {', '.join(valid_extensions)}")
    
class UserImports(models.Model):
    user = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, blank=True, null=True, related_name="user_imports")
    title = models.CharField(max_length=500, null=True, blank=True)
    content = CKEditor5Field('content', config_name='extends', null=True, blank=True)
    content2 = CKEditor5Field('content', config_name='extends', null=True, blank=True)
    
    file = models.FileField(validators=[validate_file_extension], null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_file = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    
class UserIntegration(models.Model):
    user = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, blank=True, null=True, related_name="user_integration")
    app_name = models.CharField(max_length=500, null=True, blank=True)
    token = models.CharField(max_length=1000)
    
    



