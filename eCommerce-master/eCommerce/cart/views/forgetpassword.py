from django.views import  View
from django.shortcuts import render , redirect
from cart.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import string
import random
from django.core.mail import EmailMessage

class Forget_password(View):

    def get(self , request):
        len_cart = 0
        try:
            cart = request.session.get("cart")
            if cart:
                len_cart = len(cart)
        except:
            pass

        cart_prod = {
            'len': len_cart,
        }
        return render(request , "forget_password.html", cart_prod)

    def post(self, request):

        email = request.POST.get('user-email')
        customer = Customer.get_customer_by_email(email)


        if customer:

            new_password = self.random_password()

            customer.password = new_password
            customer.password = make_password(customer.password)
            customer.register()

            email = EmailMessage('New Password', f'Your new password is :"{new_password}" . ', to=[email])
            email.send()

            error_message = "Your password send to your registered email !! "
            messages.success(request, error_message)
            return redirect("home")

        else:
            error_message = "Please check your email and re-enter your registered email !! "
            messages.error(request, error_message)
            return redirect("forget_password")

    def random_password(self):

        LETTERS = string.ascii_letters
        NUMBERS = string.digits
        PUNCTUATION = '@#$&'

        printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
        printable = list(printable)
        random.shuffle(printable)
        random_password = random.choices(printable, k=10)
        random_password = ''.join(random_password)

        return random_password


