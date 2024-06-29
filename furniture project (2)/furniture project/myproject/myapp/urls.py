from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("about/", views.about, name="about"),
	path("contact/", views.contact, name="contact"),
	path("services/", views.services, name="services"),
	path("shop/", views.shop, name="shop"),
	path('show_product/', views.show_product, name='show_product'),
	path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
	path("thankyou/", views.thankyou, name="thankyou"),
	path("checkout/", views.checkout, name="checkout"),
	path("register/", views.register, name="register"),
	path("login/", views.login, name="login"),
	path('logout/', views.logout, name='logout'),
]