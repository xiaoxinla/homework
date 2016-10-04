from django.conf.urls import url
from . import views

app_name = 'dbpro'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'shop/(?P<pk>[0-9]+)/$', views.ShopView.as_view(), name='shop'),
    url(r'user/(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'commodity/(?P<pk>[0-9]+)/$', views.CommodityView.as_view(), name='commodity'),
    url(r'cart/(?P<pk>[0-9]+)/$', views.CartView.as_view(), name='cart'),
    url(r'order/(?P<pk>[0-9]+)/$', views.OrderView.as_view(), name='order'),
    url(r'register/$', views.register, name='register')
]

