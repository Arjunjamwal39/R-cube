from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator
from sympy import false, product, true
from phonenumber_field.modelfields import PhoneNumberField

STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("Assam","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("Punjab","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("West Bengal","West Bengal")
)

ADDRESS_TYPEE = (
    ('Home','Home'),
    ('Office','Office'),
    ('Others','Others'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    Contact_number = PhoneNumberField()
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    address_type = models.CharField(choices=ADDRESS_TYPEE, max_length=50, default='')

    def __str__(self):
        return str(self.id) #default generated

CATEGORY_CHOICE = (
    ('E','Eatables'),
    ('C','Clothing'),
    ('F','Furniture'),
    ('H','Home_decor'),
    ('L','Latest'),
    ('S','Slider',)
)

PRODUNIT = (('kg','kg'),
            ('litre','litre'),
            ('unit','unit'),
)
class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    unit = models.CharField(max_length=50, choices=PRODUNIT, default='Nil')
    discription = models.TextField()
    product_image = models.ImageField(upload_to='productimg')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2, default='')
    brand = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def mrp(self):
        return self.quantity * self.product.price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def mrp(self):
        return self.quantity * self.product.price

class practice(models.Model): #extrassss
    title = models.CharField(max_length=30, null=True,default='')
    discription = models.TextField(null=True,default='')
    imagee = models.ImageField(upload_to='productimg',default='')

class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()


stat = {('free','free'),
        ('duty','duty'),
        ('took off','took off'),
}
class Deliveryboy(models.Model):
    Name = models.CharField(max_length=50)
    Contact_number = PhoneNumberField()
    discription = models.TextField(null=True)
    stat = models.CharField(max_length=50, choices=stat, default='duty')
    emaill = models.EmailField(default='')
    def __str__(self):
        return str(self.id)