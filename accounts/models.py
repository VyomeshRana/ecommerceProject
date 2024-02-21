from django.db import models

# Create your models here.

class customerModel(models.Model):
    username = models.CharField(max_length=50)
    f_name = models.CharField(max_length=100,default=None, blank=True, null=True)
    L_name = models.CharField(max_length=100,default=None, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phoneNo = models.IntegerField()
    address1 =  models.CharField(max_length=200)
    address2 =  models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    password = models.CharField(max_length=20)
    confPass = models.CharField(max_length=20)

    
    def __str__(self):
        return self.username
    
    

class vendorModel(models.Model):
    name =     models.CharField(max_length=50)
    shopName =  models.CharField(max_length=50)
    shopAddress = models.CharField(max_length=50)
    shopLicence = models.ImageField(upload_to='Licence', blank=True )
    longitude = models.FloatField()
    latitude = models.FloatField()
    vendorMail = models.EmailField(max_length=254)
    vendorPhone = models.IntegerField()
    password = models.CharField(max_length=20)
    confPass = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

