from django.contrib import admin
from .models import Hood, Business, Admin

# Register your models here.
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(Admin)