from django.contrib import admin
from accounts.models import Customer
from accounts.models import Product
from accounts.models import Tags
from accounts.models import Orders

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tags)
admin.site.register(Orders)
# Register your models here.
