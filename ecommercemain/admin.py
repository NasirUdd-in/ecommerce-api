from django.contrib import admin
from .models import UserProfile, User, Status, Customer, SellerType

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Customer)
admin.site.register(SellerType)
