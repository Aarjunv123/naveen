from rest_framework import viewsets
from cart.serializers import Category_serilizer, Customer_serilizer, Contact_serilizer, Product_serilizer , Oreder_serilizer
from cart.serializers import Cart_serilizer, Billing_serilizer, Cancel_order_serilizer, Replace_serilizer, Subscriber_serilizer
from cart.models.category import Category
from cart.models.customer import Customer, Cart
from cart.models.contact_us import Contact
from cart.models.product import Product
from cart.models.orders import Orders
from cart.models.billing import Billing
from cart.models.cancle_order import Cancel_order
from cart.models.replace import Replace
from cart.models.subscribers import Subscriber

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_serilizer
    http_method_names = ['get']


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customer_serilizer
    http_method_names = ['get', 'post']

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = Contact_serilizer
    http_method_names = ['get', 'post']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_serilizer
    http_method_names = ['get']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = Oreder_serilizer
    http_method_names = ['get', 'post']

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = Cart_serilizer
    http_method_names = ['get', 'post']

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = Billing_serilizer
    http_method_names = ['get', 'post']

class Cancel_orderViewSet(viewsets.ModelViewSet):
    queryset = Cancel_order.objects.all()
    serializer_class = Cancel_order_serilizer
    http_method_names = ['get', 'post']

class ReplaceViewSet(viewsets.ModelViewSet):
    queryset = Replace.objects.all()
    serializer_class = Replace_serilizer
    http_method_names = ['get', 'post']

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = Subscriber_serilizer
    http_method_names = ['get', 'post']