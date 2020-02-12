from django.template import loader
from django.shortcuts import render
from service.models import Product,Category



def main(request):
    product = Product.objects.filter(available=True)
  #  template = loader.get_template('service/main.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    cat = Category.objects.all()
    return render(request, 'service/main.html', {
            'product': product,
            'cate':cat,
        })


