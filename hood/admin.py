from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Hood, Business, Admin, User

# Register your models here.
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(Admin)
admin.site.register(User, UserAdmin)