from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# from django.urls import resolvers

# Create your models here.

#Extending User model with one to one fields 
class userProfiles(models.Model):
    # AUTH_PROFILE_MODULE = 'regiuser.userProfile'
    user = models.OneToOneField(User, related_name='userProfile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    address = models.TextField(max_length=500, null=True)
    DOB = models.DateField(blank=True, null=True)
    userType = models.CharField(max_length=12, default='Customer')

    def __str__(self):
        return str(self.user)

class sellerProfile(models.Model):
    userSeller = models.OneToOneField(User, related_name='sellerProfile', on_delete=models.CASCADE)
    phoneSeller = models.CharField(max_length=12, blank=True)
    addressSeller = models.TextField(max_length=500, null=True)
    userType = models.CharField(max_length=12, default='Seller')

    def __str__(self):
        return str(self.userSeller)

class herbProduct(models.Model):
    sellername = models.ForeignKey(sellerProfile, on_delete=CASCADE)
    productName = models.TextField(max_length=150)
    productImage = models.ImageField(null=True, blank=True, upload_to="images/")
    productPrice = models.FloatField(default=0.00)
    productDesc = models.TextField()

    def __str__(self):
        return str(self.sellername)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         userProfiles.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userProfiles.save()