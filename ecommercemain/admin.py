from django.contrib import admin
from .models import UserProfile, User, Status, Customer

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Customer)
