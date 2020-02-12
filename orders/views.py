from django.shortcuts import render,redirect
from .models import OrderItem,Order,OrderDis
from service.models import Shop
from .forms import OrderCreateForm
from service.cart import Cart
from django.contrib.auth.decorators import login_required
from orders.models import Order
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from random import random
import random
from random import choice
from string import ascii_lowercase
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
MERCHANT_KEY='f!zqdoLJqnR01wrz'

@login_required(login_url='/accounts/login_user')
def order_create(request, pk):
        cart = Cart(request)
        a=0

        oo=choice(ascii_lowercase)
        oo=oo.upper()
        print(oo.islower())
        print(choice(ascii_lowercase))

        print(random.randint(100, 999))
        print("hiiiii")
        for item in cart:
            a=a+1
        if a == 0:
            item=0
        order=0
        if a != 0:

            b = item
            ids = b['id']
            g = get_object_or_404(Shop, pk=int(ids))
            shopn=g.name
            print(g.name)

        if  a != 0 :
            a = sum(Decimal(item['price']) * 1 for item in cart.cart.values())
            b = sum(Decimal(item['b_price']) * 1 for item in cart.cart.values())
            nos = 1
            tshopc = nos * a
            s = (b - a) * nos

            if b == 0:
                p = 0

            else:
                p = round(Decimal(s / b * 100), 2)

            if request.method == 'POST':
                form = OrderCreateForm(request.POST)

          #      off=sum(Decimal(item['price']) * item['quantity'] for item in cart) - (
            #        sum(Decimal(item['price']) * item['quantity'] for item in cart)) / 10
           #     poff=cart.get_saved()+10
#                if form.is_valid():
                name = request.POST.get("name")
                pno = request.POST.get("pno")
                email = request.POST.get("addr")
                date = request.POST.get("date")
                time = request.POST.get("time")
                print(pno)
                print("pno")
                ordr = Order()
                ordr.addr = email
                ordr.user = request.user
                ordr.name = name
                ordr.phone_no = pno
                ordr.date = date
                ordr.timing = time
                ordr.num=nos
                print(pno)
                print(ordr.date)
                print(ordr.timing)
                print(ordr.addr)
                print(ordr.phone_no)

                #order = form.save()
                ordr.user=request.user
                ordr.total_cost=sum(Decimal(item['price']) * item['quantity'] for item in cart)

            #       z=(sum(Decimal(item['price']) * item['quantity'] for item in cart))/10   -z below
                ordr.total_a_cost=sum(Decimal(item['price']) * item['quantity'] for item in cart)

                ordr.shop=g
                print(g)
                ordr.save()
                print("abhit above")

                ordr.o_id=order_id(ordr)

                for item in cart:
                    OrderItem.objects.create(
                        order=ordr,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'],
                        total_i_price=item['price']*item['quantity']
                    )

                ordr.save()
                cart.clear()

                print(ordr.name)
                param_dict={
                    'MID': 'oLhXxv07209903445994',
                    'ORDER_ID': str(ordr.o_id),
                    'TXN_AMOUNT':str(ordr.total_a_cost) ,
                    'CUST_ID': request.user.email,
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8000/orders/handlerequest/'
                }
                param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

                #request paytm to tranfer teh amount to your account after payment by user
                #return render(request, 'orders/order/created.html', {'order': ordr})
                return render(request,'orders/order/paytm.html',{'param_dict':param_dict})

            else:
                form = OrderCreateForm()

            return render(request, 'orders/order/create.html', {'form': form,'shop':g,'shopc':tshopc,'no':nos})

        else:
            return redirect('/service/detail/'+pk+'/')


@login_required(login_url='/accounts/login_user')
def order_create_cod(request, pk):
        cart = Cart(request)
        a=0

        oo=choice(ascii_lowercase)
        oo=oo.upper()


        for item in cart:
            a=a+1
        if a == 0:
            item=0
        order=0
        if a != 0:

            b = item
            ids = b['id']
            g = get_object_or_404(Shop, pk=int(ids))

            shopn=g.name
            print(g.name)

        if  a != 0 :
            a = sum(Decimal(item['price']) * 1 for item in cart.cart.values())
            b = sum(Decimal(item['b_price']) * 1 for item in cart.cart.values())
            nos = 1
            tshopc = nos * a
            s = (b - a) * nos

            if b == 0:
                p = 0

            else:
                p = round(Decimal(s / b * 100), 2)

            if request.method == 'POST':
                form = OrderCreateForm(request.POST)

                name = request.POST.get("name")
                pno = request.POST.get('pno')
                email = request.POST.get("addr")
                date = request.POST.get("date")
                time = request.POST.get("time")
               # print(email+"before")
                print(request.user.email)
                print("pno")
                print(pno)


                ordr = Order()
                ordr.addr = email
                ordr.user = request.user
                ordr.name = name
                ordr.phone_no = pno
                ordr.date = date
                ordr.timing = time
                ordr.num=nos

                #order = form.save()
                ordr.user=request.user
                ordr.total_cost=sum(Decimal(item['b_price']) * item['quantity'] for item in cart)

            #       z=(sum(Decimal(item['price']) * item['quantity'] for item in cart))/10   -z below
                ordr.total_a_cost=sum(Decimal(item['price']) * item['quantity'] for item in cart)

                ordr.shop=g
                print(g)
                ordr.save()
                print("abhit above")

                ordr.o_id=order_id(ordr)

                for item in cart:
                    OrderItem.objects.create(
                        order=ordr,
                        product=item['product'],
                        price=(item['b_price']),
                        quantity=item['quantity'],
                        total_i_price=int(item['price']),
                    )
                cart.clear()

                ordr.save()

                return render(request, 'orders/order/created.html', {'order': ordr})


            else:
                form = OrderCreateForm()

            return render(request, 'orders/order/create.html', {'form': form,'shop':g,'shopc':tshopc,'no':nos})

        else:
            return redirect('/service/detail/'+pk+'/')



def order_id(order):
    id=order.id
    n=(order.name).lower()
    n=n[:1].lower()
    print(n)
    s1=choice(ascii_lowercase)
    s2=choice(ascii_lowercase)

    u=n[:1]
    if id < 10:
        print()
        ran= random.randint(100, 999)

    elif id >= 10 and id < 100 :
        ran= random.randint(10, 99)

    elif id >= 100 and id < 1000:
        ran= random.randint(1, 9)

    else:
        ran = 0

    if ran != 0:
        o_id=n+s1+str(id)+s2+str(ran)
    else:
        o_id=n+s1+str(id)+s2+str(ran)

    print(o_id)
    print("ayush above")
    return o_id

def delete_order(request, pk):
   #album = get_object_or_404(Album, pk=album_id)
    order = Order.objects.get(pk=pk)
    if order.paid == True:
        print("paid")
    else:
        order.delete()

    return redirect('orders:your_order')


# return render(request, 'orders/order/your_order.html', {'orders': orders, 'order_items': order_items})


@login_required(login_url='/login_user')
def your_order(request):
    orders = Order.objects.filter(user=request.user)

    order_items=OrderItem.objects.all()

    order_dis=OrderItem.objects.all()
    return render(request,'orders/order/your_order.html', {'orders':orders,'order_dis':order_dis})

@login_required(login_url='/login_user')
def order_created(request):
    return render(request, 'orders/order/created.html')


'''
                    OrderDis.objects.create(
                        order=order,
                        name='10%_discount',
                        total_dis=p+10,
                        total_saved_rs=cart.get_t_saved_rs(),
                        extra_dis=z,
                    )
'''
@csrf_exempt
def handlerequest(request):
#paytm will send post request
    form=request.POST
    response_dict={}
    verify=False
    checksum=0
    for i in form.keys():
        response_dict[i]=form[i]
        if i == 'CHECKSUMHASH':
            checksum=form[i]
    if checksum == 0:
        return redirect("/")

    verify=Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order Succesful')
            order = Order.objects.get(o_id=response_dict['ORDERID'])
            order.paid= True
            order.save()
            print("order id is")
            print(response_dict['ORDERID'])
        else:
            print("Not Succsefull")
            order = Order.objects.get(o_id=response_dict['ORDERID'])
            delete_order(request,order.id)


    return render(request,'orders/order/paymentstatus.html',{'response':response_dict})
