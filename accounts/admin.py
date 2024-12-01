from django.contrib import admin
from .models import Account, UserImports,UserIntegration
# Register your models here.


admin.site.register(Account)
admin.site.register(UserImports)
admin.site.register(UserIntegration)
