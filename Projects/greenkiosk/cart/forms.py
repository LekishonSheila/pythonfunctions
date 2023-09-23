from django import forms
from .models import Product_Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Product_Cart
        fields = ['item_id', 'item_name','price','quantity','date_added'] 