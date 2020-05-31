from django.contrib import admin
from .models import EmailModel,Users
# Register your models here.

admin.site.register(EmailModel)
admin.site.register(Users)