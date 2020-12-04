from rest_framework import serializers
from .models.category import Category
from .models.customer import Customer, Cart
from .models.contact_us import Contact
from .models.product import Product
from .models.orders import Orders
from .models.billing import Billing
from .models.cancle_order import Cancel_order
from .models.replace import Replace
from .models.subscribers import Subscriber
from django.contrib.auth.hashers import make_password

class Category_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Customer_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_name', 'phone', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer.objects.create(
               customer_name=validated_data['customer_name'],
                email=validated_data['email'],
                phone=validated_data['phone'],
                password=validated_data['password']
                                        )
        user.password = make_password(user.password)
        user.save()
        return user


class Contact_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class Product_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Oreder_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class Cart_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class Billing_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'

class Cancel_order_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancel_order
        fields = '__all__'

class Replace_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Replace
        fields = '__all__'

class Subscriber_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'









