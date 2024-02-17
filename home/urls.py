from django.urls import path
from .import views
urlpatterns=[
    path("",views.home,name='home'),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("product/",views.products,name="product"),
    path("cart/<int:id>",views.carts,name="cart"),
]