from django.contrib import admin
from .models import Hood, User, Business

# Register your models here.
admin.site.register(Hood)
admin.site.register(User)
admin.site.register(Business)