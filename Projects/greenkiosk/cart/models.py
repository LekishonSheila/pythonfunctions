from django.db import models

# Create your models here.
class Cart(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6,decimal_places=3)
    quantity = models.PositiveBigIntegerField()
    total_price = models.DecimalField(max_digits=7,decimal_places=2)
    date_added = models.IntegerField()
    product_image = models.ImageField()
