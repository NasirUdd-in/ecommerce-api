from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField



class Status(models.Model):
    status_name = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return self.status_name
    
    
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    status = models.OneToOneField(Status, on_delete=models.CASCADE, blank=True, null=True)
    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Vendor'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role


class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # def full_address(self):
    #     return f'{self.address_line_1}, {self.address_line_2}'

    def __str__(self):
        return self.user.email

class Customer(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.OneToOneField(Status, on_delete=models.CASCADE, blank=True, null=True)
    authorized_user_id = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.authorized_user_id
    
class SellerType(models.Model):
    status = models.OneToOneField(Status, on_delete=models.CASCADE, blank=True, null=True)
    seller_type_name = models.CharField(max_length=45, blank=True, null=True)
    max_product_limit = models.CharField(max_length=255, blank= True, null= True)
    
    def __str__(self):
        return self.seller_type_name
    
class Seller(models.Model): 
   user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
   status = models.OneToOneField(Status, on_delete=models.CASCADE, blank=True, null=True)
   store_name = models.CharField(max_length = 45)
   seller_type = models.OneToOneField(SellerType, on_delete=models.CASCADE, blank= True, null=True )
   authorized_user_id = models.CharField(max_length=255, blank=True, null=True)
   
class Category(models.Model):
   seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
   status = models.OneToOneField(Status, on_delete=models.CASCADE, blank=True, null=True)
   category_name = models.CharField(max_length=60)
   description = models.CharField(max_length=60)
   
class Size(models.Model):
   size_title = models.CharField(max_length=60)
    
class Color(models.Model):
   color_title = models.CharField(max_length=60)
   

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    status = models.OneToOneField(Status, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_in_hand = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def total_items(self):
        return sum(item.quantity for item in self.cart_items.all())

    def total_price(self):
        return sum(item.subtotal for item in self.cart_items.all())

    def __str__(self):
        return f"Cart for {self.customer.user.username}"