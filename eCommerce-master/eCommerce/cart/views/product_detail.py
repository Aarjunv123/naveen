from django.views import  View
from django.shortcuts import render
from cart.models.product import Product

class Product_detail(View):

    def get(self , request , id):
        len_cart = 0
        try:
            cart = request.session.get("cart")
            if cart:
                len_cart = len(cart)
        except:
            pass

        prod = Product.objects.get(id=id)
        prodname = prod.name
        print(f"prodname 1 {prodname}")
        prodname = prodname.split("_")
        print(f"prod name {prodname}")
        related_prod = Product.objects.filter(name__icontains=prodname[0])
        print(f"all Prod {related_prod}")

        ids =[]
        try:
            if request.session.get("cart"):
                ids = list(request.session.get('cart').keys())
        except:
            pass
        flag = ""
        if str(id) in ids:
            flag = 1
        my_product = {
            'product': prod,
            'flag' : flag,
            'len': len_cart,
            'related_prod':related_prod

                }
        return render(request , 'product_view.html', my_product)
