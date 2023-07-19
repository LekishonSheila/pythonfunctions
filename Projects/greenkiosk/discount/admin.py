from django.contrib import admin
from .models import discount

# Register your models here.
class discountAdmin(admin.ModelAdmin):
    list_display = ("discount", "name", "items_bought", "active", "date")
admin.site.register(discount, discountAdmin)
