from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product

# Create your views here.
 
def product_upload_view(request):
    form = ProductUploadForm()
    return render(request, "inventory/product_upload.html",{"form":form})

def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html", {"products": products})

def productdetailview(request):
    product = Product.objects.get(id=id)
    return render(request, "inventory/product_details.html", {"product": product})

def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            product = Product.objects.get(pk=product_id)

            cart_item = {
                'product': product,
                'quantity': quantity,
            }

            if 'cart' not in request.session:
                request.session['cart'] = []

            request.session['cart'].append(cart_item)

            return redirect('cart')  

    else:
        form = add_to_cart()
    return render(request, "inventory/add_to_cart.html", {"form": form})



def edit_product_view(request,id):
    product=Products.objects.get(id=id)
    if request.method=='POST':
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("product_details_view",id=product.id)
    else:
        form = ProductUploadForm(instance=product)
        return render(request,"inventory/edit_product.html",{"form",form})


def cart_list(request):
    cart=Product.objects.all()
    return render(request,"inventory/cartlist.html",{"cart":cart_list})


