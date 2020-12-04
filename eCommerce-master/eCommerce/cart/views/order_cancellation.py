from django.views import  View
from django.shortcuts import render , redirect
from cart.models.customer import Customer
from cart.models.orders import Orders
from cart.models.cancle_order import Cancel_order
from datetime import datetime


class Order_cancel(View):
    def get(self, request, id):

        try:
            user = request.session.get('customer_id')
        except:
            user = False
        if user:
            len_cart = 0
            try:
                cart = request.session.get("cart")
                if cart:
                    len_cart = len(cart)
            except:
                pass
            order = Orders.get_order_by_id(id)
            if order:
                if order.status == 'Ordered':
                    cart_prod = {

                        'len': len_cart,
                        'order': order
                    }
                    return render(request, 'cancellation_form.html',cart_prod)
                else:
                    return redirect('profile')
            else:
                return redirect('profile')
        else:
            return redirect('home')

    def post(self, request):
        customer = request.session.get('customer_id')
        order_id = request.POST.get('order_id')
        name =  request.POST.get('name')
        phone =  request.POST.get('phone')
        email =  request.POST.get('email')
        reason =  request.POST.get('reason')


        cancel = Cancel_order(customer= Customer(id=customer),
                              order_id= order_id, name=name, phone=phone, email=email, reason=reason)
        cancel.save()
        order = Orders.get_order_by_id(int(order_id))
        order.status = "Cancelled"
        order.order_delevered_date = datetime.now()
        order.register()

        return redirect('profile')
