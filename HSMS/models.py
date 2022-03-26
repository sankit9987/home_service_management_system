from distutils.command.upload import upload
from xml.sax.handler import feature_external_ges
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("email is required"))
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("super user is "))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("super user is "))
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    is_service = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
    objects = UserManager()


class service_category(models.Model):
    name = models.CharField(max_length=100)
    createdat=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} {self.id}"
    
class subcategory(models.Model):
    category=models.ForeignKey(service_category,on_delete=models.CASCADE)
    sub_category_name=models.CharField(max_length=50)
    createdat=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.sub_category_name}"

class Service_provider(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category=models.ForeignKey(service_category,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.TextField()
    mobile_no = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.TextField()
    image = models.ImageField(upload_to="adhar",null=True)
    mobile_no = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = UserManager()



class service(models.Model):
    category=models.ForeignKey(service_category,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Service_provider,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    service_sub_category=models.ForeignKey(subcategory,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=5000,null=True)
    description=models.TextField(null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    discount=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    image=models.ImageField(upload_to="service_image",null=True)
    feature=models.CharField(max_length=5000,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
st = (
    ('Order','Order'),
    ('Pending','Pending'),
    ('Cencel','Cencel'),
)
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    ser = models.ForeignKey(service, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(Service_provider, on_delete=models.CASCADE,null=True)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100,  choices=st)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)



class Feedback(models.Model):
    serv = models.ForeignKey(service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    msg = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)