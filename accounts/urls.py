from django.contrib import admin
from django.urls import path,re_path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('signup/',views.signup),
    path('customersignup', views.customersignup),
    path('',views.home),
    path('signin/', views.signin),
    path('customersignin', views.customersignin),
    path('cart', views.carts),
    path('logout', views.logout),
    path('updatecart', views.updatecart),
    path('checkout', views.checkout),
    path('yourorder', views.yourorder),
    path('orderlist', views.orderlist),
    re_path(r'^product/(?P<catid>\d+)/$', views.productsView),
    re_path(r'^yourorder/(?P<oid>\d+)/$', views.yourorder),
    re_path(r'^removeitem/(?P<pid>\d+)/$', views.removeitem),
    re_path(r'^cart/(?P<pid>\d+)/$', views.itemadded),
]
