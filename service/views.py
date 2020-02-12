from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic import View
from .models import Category,Product,Shop,Facility,Feedback
from .cart import Cart
from django.template import loader
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout,get_user_model
from .forms import Feedbackform
from django.contrib.auth import get_user_model
from django.utils.http import is_safe_url
from django.http import JsonResponse
from decimal import Decimal

User = get_user_model()

from django.contrib.auth.decorators import login_required




from .forms import CartAddProductForm




def Vindex(request):
    album = get_object_or_404(Category, pk=2)
    cart_product_form = CartAddProductForm()
    shop=Shop.objects.all()
    # template = loader.get_template('music/index.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    return render(request, 'service/index.html', {'album': album, 'type':shop, 'cart_product_form':cart_product_form})



def Findex(request):
    cart=Cart(request)
    album = get_object_or_404(Category, pk=1)
    cart_product_form = CartAddProductForm()
    fac=Facility.objects.all()
    # template = loader.get_template('music/index.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    return render(request, 'service/index.html', {'album': album, 'type': fac , 'cart_product_form':cart_product_form,'cart':cart})


def Bindex(request):
    album = get_object_or_404(Category, pk=3)
    cart_product_form = CartAddProductForm()
    # template = loader.get_template('music/index.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    return render(request, 'service/index.html', {'album': album, 'type':"Beverages", 'cart_product_form':cart_product_form})


def Sindex(request):
    cart=Cart(request)
    album = get_object_or_404(Category, pk=4)
   # cart_product_
    form = CartAddProductForm()
    # template = loader.get_template('music/index.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    return render(request, 'service/index.html', {'album': album, 'type':"Snacks", 'cart_product_form':'cart_product_form','cart':cart})



def detail(request, album_id):
    album = get_object_or_404(Shop, pk=album_id)
    cart_product_form = CartAddProductForm()

    return render(request, 'service/detail.html', {'service': album ,'cart_product_form': cart_product_form})
    #in this we will get albumname_albumartist as becouse we done in models to give only title f album then doalbum.album_title


def is_valid_queryparam(param):
    return param !='' and param is not None

def sfood(request):
    category = Category.objects.all()
    shop = Shop.objects.all()
    prod=Product.objects.all()
    template = loader.get_template('service/sfood.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    cart_product_form = CartAddProductForm()
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    print(price_min)
    print(price_max)

    query = request.GET.get("q")

    if query:
        category = category.filter(
            Q(name__icontains=query) |
            Q(nick_names__icontains=query)
        ).distinct()

        shop = shop.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(nick_names__icontains=query) |
            Q(city__icontains=query)
        ).distinct()


    if is_valid_queryparam(price_min):
        prod=prod.filter(price__gte=price_min)
        a = []
        i = 0
        for s in shop:
            print(s)
            print(s.product_set.all())
            print("hello")

            for p in prod:

                if(p in s.product_set.all()):
                    a.append(s)
                    print("yes it is there")
                    i=i+1
                    break

        print(prod)
        shop = a

        print("fdkajfakjfadkjkldfj")
        print(a)
        print("ananfkdjnakfjnajk")

    if is_valid_queryparam(price_max):
        prod=prod.filter(price__lte=price_max)
        a = []
        i = 0
        for s in shop:
            print(s)
            print(s.product_set.all())
            print("hello")

            for p in prod:

                if(p in s.product_set.all()):
                    a.append(s)
                    print("yes it is there")
                    i=i+1
                    break
        print(prod)

        print("fdkajfakjfadkjkldfj")
        print(a)
        print("ananfkdjnakfjnajk")
        shop = a

    for z in shop:
        print(z.city)
        print(z)
    print(shop)
    print("final  result")


    return render(request, 'service/sfood.html', {
        'category': category,
        'shop': shop,
        'cart_product_form': cart_product_form,
    })



def about_us(request):
    return render(request,'service/about.html',{'service':"ayush",})

def contact_us(request):
    return render(request,'service/contact.html',{'service':"contact",})


def services(request):
    return render(request,'service/service.html',{'service':"contact",})


'''
def cart_create(user=None):
    cart_obj=Cart.objects.create(user=None)
    print('new cart creted')
    return cart_obj

def cart_home(request):
    #del request.session['cart_id']
    request.session['cart_id']=int("12")#we set y default that d is thre whether it belongs to ue or not
    cart_id=request.session.get("cart_id",None)
#we are creatin
    # g nione user because to stor data of outsiders withoue loginuserrs

    if cart_id is None:# and isinstance(cart_id,int):
        cart_obj=cart_create()
        request.session['cart_id']=cart_obj.id
    else:
        qs=Cart.objects.filter(id=cart_id)#this means catr exist adn wherther t has data or nt it checks

        if qs.count()==1:#check thrt therr i s any cart daa or nto or its object
            print('cart id exist')
            cart_obj=qs.first()
        else:
            cart_obj=cart_create()#if threr is no data then create
            request.session['cart_id']=cart_obj.id#this taes the above id only


    return render(request,"service/carts.html",{})

'''


@require_POST
def cart_up(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)


    if request.is_ajax():
        print("entered")
        data={}
        #cd = form.cleaned_data
        print(request.POST.get('val'))
        val=(request.POST.get('val'))

        print("above")
        cart.add(product=product, quantity=int(val), update_quantity=True)
        a = cart.get_total_price()
        s = cart.get_saved()
        data={
          'message':"form saved",
          'id': product_id,
          'errordata':"data erroaved",
          'total':a,
           'b_total': s,
        }
        return JsonResponse(data)
    return redirect('service:cart_detail')

def cart_del(request):
    cart=Cart(request)
    cart.clear()
    return redirect('service:cart_detail')


@require_POST
def cart_ar(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print("entered in view")
    a = 0

    print("neters inajax form")
    i = product_id+''
    for k in cart.cart.keys():
        print(k)
        print("is is above")
    if i in cart.cart.keys():
        cart.remove(product)
        a = cart.get_total_price()
        q=0
        data = {
            'message': "removed frrom cart",
            'errordata': "data erroaved",
            'id': product_id,
            'total': a,
            'q':q,
        }
    else:
        if form.is_valid():
            cd = form.cleaned_data
            cng = 'no'
            for item in cart.cart.values():
                print(item)
                a = a + 1
            print(cart.cart.keys())
            print("caheck this above is keys")
            d=0
            if a != 0:
                print("not a1st item")
                shop=product.shops
                print(shop.id)
                b = item
                print(b['id'])
                d=b['id']
                print("this is the sshop id=")
                if int(b['id']) == shop.id:
                    print('true')
                else:
                    cart.empty()
                    cng='yes'
                    print("wrong items in cart")
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
            a = cart.get_total_price()
            b = cart.get_b_total_price()
            s=(b-a)/b*100
            q=1
            data={
              'message':"Added to cart",
              'id': product_id,
              'errordata':"data erroaved",
              'total':a,
              'q':q,
              'cng':cng,
              'sid':d,
             }
        data={}
        return redirect('service:cart_detail')

    return redirect('service:cart_detail')



def ref(request):
    cart=Cart(request)
    if request.is_ajax():
        a=[]
        for i in cart.cart.keys():
            a.append(i)

#        p = get_object_or_404(Product, id=i)
#        print(p.shops.id)
#        print("aboveis shop")
#        print(i)
#
#        print("hi iiiiiii an ashi...")
#        print(a)
        data={
            'ids':a,
  #          's_id':p.shops.id,
        }
        return JsonResponse(data)



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        print("adding in cart")

    return redirect('service:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)
    a = cart.get_total_price()

    return redirect('service:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    a=0

    if request.is_ajax():
        a = cart.get_total_price()
        s=cart.get_saved()

        for i in cart:
            print(i)

        data = {
                  'message':"form saved",
                  'errordata':"data erroaved",
                  'total':a,
                   'saved':s,
        }
        return JsonResponse(data)

    message = ''
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
        a += 1
    if a == 0:
        message='Please Add item to the cart before shopping'

    return render(request, 'service/cart_detail.html', {'cart': cart,'message':message})


def feedback(request):
    print(request.method)
    if request.method == "POST":
        email = request.POST.get("email")
        feedback = request.POST.get("message")
        name = request.POST.get("name")
        sub = request.POST.get("subject")

        if email == "" or feedback == "":
            error_message = "dont left empty"
        else:
            feed=Feedback()
            feed.email=email
            feed.name=name
            feed.sub=sub



            feed.feedback=feedback
            print(email,feedback)
            feed.save()
            return redirect("/")

    else:
        error_message='fill coorectly'

    return render(request, "service/feedback.html", {
        "form": 'form',
        "error_message": error_message
    })
