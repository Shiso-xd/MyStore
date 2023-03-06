from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to="store/images",
                              default="store/images/default.png")

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)
    price_origin = models.FloatField(null=True)
    image = models.ImageField(upload_to="store/images",
                              default="store/images/default.png")
    content = RichTextUploadingField(blank=True, null=True)
    public_day = models.DateTimeField(default=datetime.datetime.now)
    viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=500, unique=False)

    def __str__(self):
        return self.username

class Client(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=250, unique=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=250, unique=False)
    image = models.ImageField(upload_to="store/images/", default="stories/images/people_default.png")

    def __str__(self):
        return self.username

class UserProfileInfo(models.Model):
    # Create relationship from this class to user
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    # Add any more attribute you want
    address = models.CharField(max_length=250, unique=False)
    phone = models.CharField(max_length=250)
    image = models.ImageField(upload_to= "store/images/", default="store/images/people_default.png")

    def __str__(self):
        return self.user.username