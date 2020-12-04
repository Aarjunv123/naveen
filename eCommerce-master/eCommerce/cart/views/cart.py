from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.views import  View
from cart.models.product import Product

class Cart(View):
    def get(self , request):
        len_cart = 0
        products = ""
        flag = ""
        try :
            cart = request.session.get("cart")
            print(cart)
            if cart:
                len_cart=len(cart)
                flag = 1
        except:
            flag = False
        if flag == 1:
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
        cart_prod = {
            "pro": products,
            'len': len_cart
        }
        return render(request, 'cart.html', cart_prod)

    def post(self, request):
    
        p_quantity = request.POST.get("quantity")
        p_id = request.POST.get("product_id")
        p_color = request.POST.get("product_color")

        cart = request.session.get("cart")

        if cart:
            cart[p_id] = [p_quantity, p_color]

        else:
            cart = {}
            cart[p_id] = [p_quantity, p_color]

        request.session['cart'] = cart

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_item(request, id):
    cart = request.session.pop('cart')
    cart.pop(str(id))
    request.session['cart'] = cart

    return redirect('cart')

def update_item(request):
    if request.method == 'POST':
        p_id = str(request.POST.get('p_id'))
        p_quantity = str(request.POST.get('quantity'))
        cart = request.session.pop('cart')

        cart[p_id][0] = p_quantity

        request.session['cart'] = cart

        return redirect('cart')

