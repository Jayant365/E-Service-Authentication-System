from decimal import Decimal
from django.conf import settings
from .models import Product
    

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity, update_quantity=False):

        product_id = str(product.id)
        print("this is the product id"+product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,'b_price': str(product.b_price), 'price': str(product.price),'id':str(product.shops.id)}
            print("added")
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
            print("updated")
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['b_price'] = Decimal(item['b_price'])
            item['total_b_price'] = item['b_price'] * item['quantity']


            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def total_cost(self):
        return


    def get_total_price(self):
        return round(sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()),0)

    def get_b_total_price(self):
        return round(sum(Decimal(item['b_price']) * item['quantity'] for item in self.cart.values()),0)

    def get_saved(self):
        a=sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        b=sum(Decimal(item['b_price']) * item['quantity'] for item in self.cart.values())
        s=b-a
        if b==0:
            p=0
        else:
            p = round(Decimal(s / b * 100), 2)

        return p


    def get_saved_rs(self):
        a=round(sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()),0)
        b=round(sum(Decimal(item['b_price']) * item['quantity'] for item in self.cart.values()),0)
        s=b-a
        print(s)
        return s

    def get_t_saved_rs(self):
        a=round(sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()),0)
        b=round(sum(Decimal(item['b_price']) * item['quantity'] for item in self.cart.values()),0)
        s=b-a
        q=round((sum(Decimal(item['price']) * item['quantity'] for item in self))/10,0)
        s=s+q
        print(s)
        return s

        '''   for k in ids:

   ''
           product_id = str(product.id)
           if product_id in self.cart:
               del self.cart[product_id]
               self.save()'''


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def empty(self):
        a=0
        ids={}
        for i in self.cart:
            ids[a]=i
            a=a+1


        print(ids)

        for k in ids:
            del self.cart[ids[k]]
            print(ids[k])



