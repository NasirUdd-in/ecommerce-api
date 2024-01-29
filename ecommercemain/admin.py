from django.contrib import admin
from .models import UserProfile, User, Status, Customer, SellerType,Category,Product,Cart,CartItem,Size,Color,Seller

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Customer)
admin.site.register(SellerType)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Seller)

