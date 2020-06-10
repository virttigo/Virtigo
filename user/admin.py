from django.contrib import admin
from .models import Sponsored, UserProfile, Share

# Register your models here.

admin.site.register(Sponsored),
admin.site.register(UserProfile),
admin.site.register(Share)
