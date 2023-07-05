from django.contrib import admin

# Register your models here.
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","stock","price","date_created","description","date_updated","image")

admin.site.register(Product,ProductAdmin)
