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
    path('logout', views.logout),
    re_path(r'^product/(?P<catid>\d+)/$', views.productsView),
]
