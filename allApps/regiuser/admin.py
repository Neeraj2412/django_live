from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(userProfiles)
admin.site.register(sellerProfile)
admin.site.register(herbProduct)
