from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'dbpro/index.html'
    queryset = Shop.objects.all()


class ShopView(generic.DetailView):
    model = Shop
    template_name = 'dbpro/shop.html'


class UserView(generic.DetailView):
    model = User
    template_name = 'dbpro/user.html'


class CommodityView(generic.DetailView):
    model = Commodity
    template_name = 'dbpro/commodity.html'


class CartView(generic.DetailView):
    model = Cart
    template_name = 'dbpro/cart.html'


class OrderView(generic.DetailView):
    model = Order
    template_name = 'dbpro/order.html'
