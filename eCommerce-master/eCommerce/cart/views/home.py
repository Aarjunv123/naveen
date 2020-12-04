from django.shortcuts import render , redirect , HttpResponseRedirect
from cart.models.product import Product
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        return redirect('homepage')



    def get(self , request):
        len_cart = 0
        try:
            cart = request.session.get("cart")
            print(f'cart {cart}')
            if cart:
                len_cart = len(cart)
        except:
            pass

        print(f"session {request.session.keys()}")
        weekely_prod = Product.objects.filter(type = 'weekely')
        new_arrival_prod = Product.objects.filter(type = "new")

        cart_prod = {
                'weekely': weekely_prod,
                'new_arrival': new_arrival_prod,
                 'len': len_cart,

        }
        return render(request, 'index.html', cart_prod)



