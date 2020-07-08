"""P1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from products.views import home_view, product_detail_view, add_products, dynamic_look_up,all_products

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Products/',home_view, name='Home'),
    url(r'^ProductDetails/',product_detail_view, name='ProductDetails'),
    url(r'^AddProducts/', add_products, name='Add'),
    # for dynamic url routing path is used insted of url
    path(r'LookUp/<int:my_id>/', dynamic_look_up, name='lookup'),
    path(r'AllProducts/', all_products, name = 'AllProducts'),
]
