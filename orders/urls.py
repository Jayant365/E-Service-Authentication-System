from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/(?P<pk>[0-9]+)/$', views.order_create, name='order_create'),
    url(r'^createcod/(?P<pk>[0-9]+)/$', views.order_create_cod, name='order_create_cod'),
    url(r'^order_created/$', views.order_created, name='order_created'),
    url(r'^handlerequest/$', views.handlerequest, name='handlerequest'),

    url(r'^your_order/$', views.your_order, name='your_order'),

    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_order, name='order_delete'),

]