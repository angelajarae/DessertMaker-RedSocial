from django.contrib import admin
from .models import UserProfile,Like,Save,Follower

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Like)
admin.site.register(Save)
admin.site.register(Follower)