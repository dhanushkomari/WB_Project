from django.contrib import admin
from .models import CustomUser as User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['username', 'email', 'rest', 'mobile']

admin.site.register(User, UserAdmin)
