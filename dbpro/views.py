from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import *

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'dbpro/index_detail.html'
    queryset = Shop.objects.all()


class ShopView(generic.DetailView):
    model = Shop
    template_name = 'dbpro/shop_detail.html'


class UserView(generic.DetailView):
    model = User
    template_name = 'dbpro/user_detail.html'


class CommodityView(generic.DetailView):
    model = Commodity
    template_name = 'dbpro/commodity_detail.html'


class CartView(generic.DetailView):
    model = Cart
    template_name = 'dbpro/cart_detail.html'


class OrderView(generic.DetailView):
    model = Order
    template_name = 'dbpro/order_detail.html'


def register(request):
    if(request.method == "POST"):
        uf = UserForm(request.POST)
        if(uf.is_valid()):
            name = uf.cleaned_data['name']
            filterResult = User.objects.filter(name = name)
            if(len(filterResult)>0):
                return render(request, 'dpro/register.html',{'errors':'The username has been occupied'})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                errors = []
                if(password1 != password2):
                    errors.append("password not same")
                    return render(request, 'dbpro/register.html',{"errors":errors})
                password = password1
                phone = uf.cleaned_data['phone']
                user = User(name=name, password=password, phone=phone)
                user.save()
                return render(request, 'dbpro/success.html',{'name':name,'operation':'Register'})
    else:
        uf = UserForm()
    return render(request, 'dbpro/register.html',{'uf':uf})

