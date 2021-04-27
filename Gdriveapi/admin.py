from django.contrib import admin
from . models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','date','chal','dal', 'salt', 'oil', 'honey','butter','milk')
    
admin.site.register(Product)