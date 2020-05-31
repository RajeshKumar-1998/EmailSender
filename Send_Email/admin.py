from django.contrib import admin
from .models import Email_Model,users
# Register your models here.

admin.site.register(Email_Model)
admin.site.register(users)