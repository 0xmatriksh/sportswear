from django.urls import path
from . import views

urlpatterns = [
    path('',views.jersey, name="jersey"),
    path('kit/',views.kit,name="kit"),
    path('others/',views.others,name="others"),

    path('detail/<str:pk>',views.detail,name="detail"),
    path('kit/detail/<str:pk>',views.detail,name="detail"),
    path('others/detail/<str:pk>',views.detail,name="detail"),

    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),

    path('update-order/',views.updateOrder,name="update-order"),
    path('process-order/',views.processOrder,name="process-order"),
]