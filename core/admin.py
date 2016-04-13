from django.contrib import admin
from .models import Installation, UserProfile

# Register your models here.
admin.site.register(Installation)
admin.site.register(UserProfile)