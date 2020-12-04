from django.db import  models

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.customer_name

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def get_customer_by_id(customer_id):
        return Customer.objects.get(id = customer_id)


    def isExists(email):
        if Customer.objects.filter(email = email):
            return True

        return  False

class Cart(models.Model):
    user_id = models.CharField(max_length=10, default='')
    cart = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user_id

    def register(self):
        self.save()

    @staticmethod
    def get_cart_by_user_id(user_id):
        return Cart.objects.get(user_id=user_id)

