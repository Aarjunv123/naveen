from django.views import  View
from django.shortcuts import render , redirect, reverse
from cart.models.orders import Orders
from cart.models.product import Product
from cart.models.customer import Customer
from django.contrib import messages
from cart.models.customer import  Cart
from cart.models.billing import  Billing
from .pages import card_len

from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

# MID = naveenstores@yahoo.com
#  pass = Fashion#a1@9


class Billing_shipping(View):

    def get(self , request):
        len_cart = card_len(request)

        cart = None
        cart_prod = {}
        try:
            cart = request.session.get('cart')
        except:
            pass
        if cart:
            product = []
            for id, value in cart.items():
                product.append(id)
                product.append(value)
            ids = list(request.session.get('cart').keys())
            if ids:

                products = Product.get_products_by_id(ids)

                user_address = Billing.get_bill_address_by_id(request.session.get("customer_id"))


                cart_prod = {
                "pro": products,
                'len': len_cart,
                'user_address': user_address,
                            }
                return render(request, 'billing-shipping.html', cart_prod)
        messages.error(request, "Your cart is Empty")
        return redirect('shop')



    def post(self , request):
        user_cart = request.session.get('cart')
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        state = request.POST.get('state')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal-code')
        phone = request.POST.get('phone')
        totalprice = int(request.POST.get('total_price'))

        detail = {
           'postal_code': postal_code,
           'phone': phone,
        }
        error_message = self.validateCustomer(detail)
        if error_message:
            messages.error(request, error_message)
            return render(request, 'billing-shipping.html')
        else:
            user_address = Billing.get_bill_address_by_id(request.session.get("customer_id"))
            if not user_address:
                billing_address = Billing(user = Customer(request.session.get('customer_id')),name=name, email=email, country=country, state=state,
                               address1=address1, address2=address2, city=city, zip_code=postal_code, phone=phone)

                billing_address.save()

            products = Product.get_products_by_id(list(user_cart.keys()))
            order_id =""
            for product in products:

                order = Orders(
                                customer =Customer(id=request.session.get('customer_id')),
                                product= product,color =user_cart.get(str(product.id))[1], quantity=user_cart.get(str(product.id))[0],
                                price=get_price(product,user_cart.get(str(product.id))[0]),
                                name=name, email=email, country=country, state=state,
                               address=address1+" "+address2, city=city, zip_code=postal_code,
                               phone=phone)
                order.save()
                order_id = order.order_id

            host = request.get_host()


            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount': '%.2f',
                'item_name': 'shirt',
                'invoice': '123456',
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host,
                                                   reverse('paypal-ipn')),
                'return_url': 'http://{}{}'.format(host,
                                                   reverse('payment_done')),
                'cancel_return': 'http://{}{}'.format(host,
                                                      reverse('payment_cancelled')),
            }
            return render(request, 'process_payment.html')

            # request.session.pop('cart')
            # try:
            #     user = Cart.get_cart_by_user_id(user_id=request.session.get('customer_id'))
            #     if user:
            #         user.cart = ''
            # except:
            #     pass
            # messages.success(request,f"Your order Placed Successfully Your Order id is {order_id} .")
            # return redirect('profile')




    def validateCustomer(self, detail):
        error_message = None
        if  not str(detail['postal_code']).isdigit:
            error_message = "Please Enter number in post code field "

        elif not str(detail['phone']).isdigit:
            error_message = "please enter only numbers in phone field "

        return error_message

def get_price(product, quantity):
    if product.discount_price > 0:
        return int(product.discount_price)*int(quantity)
    else:
        return int(product.price)*int(quantity)

@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')



