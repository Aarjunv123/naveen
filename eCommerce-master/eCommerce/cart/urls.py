from django.urls import path, include
from .views.home import Index
from .views.cart import Cart, delete_item, update_item
from .views.shop import Shop , Fbshop
from .views.order_cancellation import Order_cancel
from .views.replace import Replace_prod
from .views.search import Search
from .views.signup import Signup , validate_email
from .views.login import Login, logout
from .views.profile import Profile, User_billing
from .views.pages import About_us, FAQ, Contact_us, Terms, Subscribers
from .views.changepassword import Change_password
from .views.forgetpassword import Forget_password
from .views.billing_shipping import Billing_shipping, payment_canceled, payment_done
from .views.product_detail import Product_detail
from .middlewares.auth import auth_middleware

from rest_framework import routers
from .views.product_api import CategoryViewSet, CustomerViewSet, ContactViewSet, ProductViewSet, OrderViewSet
from .views.product_api import CartViewSet, BillingViewSet, Cancel_orderViewSet, ReplaceViewSet, SubscriberViewSet
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'contact_us', ContactViewSet)
router.register(r'product', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'billing', BillingViewSet)
router.register(r'cancel_order', Cancel_orderViewSet)
router.register(r'replace', ReplaceViewSet)
router.register(r'subscriber', SubscriberViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', Index.as_view(), name='home'),
    path('cart/', Cart.as_view(), name='cart'),
    path('facebookLive/', Fbshop.as_view()),
    path('facebookLive/<str:date>/', Fbshop.as_view()),
    path('facebookLive/<str:date>/<str:filter>/', Fbshop.as_view()),
    path('shop/<str:category>/', Shop.as_view(), name='shop'),
    path('shop/<str:category>/<str:subcat>/', Shop.as_view(), name='shop'),
    path('shop/<str:category>/<str:subcat>/<str:filter>/', Shop.as_view(), name='shop'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signup/validate/', validate_email, name='validate_email'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', auth_middleware(Profile.as_view()), name='profile'),
    path('profile/billing_shipping/', auth_middleware(User_billing.as_view()), name='profile-billing'),
    path('profile/order/order_cancellation/<int:id>', Order_cancel.as_view()),
    path('profile/order/order_cancellation', Order_cancel.as_view()),
    path('profile/order/order_replace/<int:id>', Replace_prod.as_view()),
    path('profile/order/order_replace', Replace_prod.as_view()),
    path('profile/change_password/', auth_middleware(Change_password.as_view()), name='change_password'),
    path('login/forget_password/', Forget_password.as_view(), name='forget_password'),
    path('cart/billing_shipping/', auth_middleware(Billing_shipping.as_view()), name='billing_shipping'),
    path('product_detail/<int:id>', Product_detail.as_view(), name='product_detail'),
    path('cart/<int:id>', delete_item, name='delete_item'),
    path('cart/update_item/', update_item, name='update_item'),
    path('about_us/', About_us.as_view(), name='about'),
    path('subscriber/', Subscribers.as_view(), name='subscribers'),
    path('contact_us/', Contact_us.as_view(), name='contact'),
    path('faqs/', FAQ.as_view(), name='faqs'),
    path('terms/', Terms.as_view(), name='terms'),
    path('search/', Search.as_view(), name='search'),
    path('logout/', logout, name='logout'),

    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),

   ]

