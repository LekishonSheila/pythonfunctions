from django.shortcuts import render
from .forms import ProductUploadForm
fromb .models import Product

# Create your views here.
 
def product_upload_view(request):
    form = ProductUploadForm()
    return render(request, "inventory/product_upload.html",{"form":form})

def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html", {"products": products})

def product_detail_view(request):
    product = Product.objects.get(id=id)
    return render(request, "inventory/product_details.html", {"product": product})


  
