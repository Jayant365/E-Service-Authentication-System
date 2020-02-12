from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

'''to craete  ne amodel maincatogorey first craete it and then makemigartions  and add it to the admi and then add ekemnts to it after add primary key in category and then ask for defulat 
 then give rimary key of your chice and migrate it fially   '''


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    nick_names = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True ,db_index=True)
    logo=models.FileField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   # class Meta:
   #     ordering = ('name', )
    #    verbose_name = 'category'
   #     verbose_name_plural = 'categories'

    def __str__(self):
        return self.name





  #  def get_absolute_url(self):
  #      return reverse('shop:product_list_by_category', args=[self.slug])



class Facility(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    icons = models.CharField(max_length=130, db_index=True)
    nick_names = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   # class Meta:
   #     ordering = ('name', )
    #    verbose_name = 'category'
   #     verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    nick_names = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)


    slug = models.SlugField(max_length=150,blank=True, unique=True ,db_index=True)
    time = models.CharField(max_length=50, db_index=True)
    maps = models.CharField(max_length=550, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo=models.FileField()
    available = models.BooleanField(default=True)
    premium = models.BooleanField(default=False)

    def __str__(self):
            return self.name



class SubCategory(models.Model):
    category = models.ForeignKey(Category  , on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True ,db_index=True)
    shopcat = models.ForeignKey(Shop , on_delete=models.CASCADE)

    nick_names = models.CharField(max_length=100, db_index=True)
    logo=models.FileField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   # class Meta:
   #     ordering = ('name', )
    #    verbose_name = 'category'
   #     verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.nick_names)


class Item(models.Model):
    category = models.ForeignKey(Category  , on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    nick_names = models.CharField(max_length=400, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True, db_index=True)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=15, db_index=True)
    available = models.BooleanField(default=True)
    logo = models.FileField()

    def __str__(self):
        return self.name



class Product(models.Model):
    user = models.ForeignKey(User  , on_delete=models.CASCADE)

    shops = models.ForeignKey(Shop , on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory , on_delete=models.CASCADE)

    prod=models.CharField(max_length=20, db_index=True)
    price = models.IntegerField()
    b_price=models.IntegerField()
    gram= models.CharField(max_length=20, db_index=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)
    logo=models.FileField()

    #class Meta:
      #  ordering = ('name', )
     #   index_together = (('id', 'slug'),)

    def __str__(self):
        return '{}'.format(self.prod+'  '+ str(self.id))

#    def get_absolute_url(self):
    #    return reverse('shop:product_detail', args=[self.id, self.slug])


def shop_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)


pre_save.connect(shop_pre_save_receiver,sender=Shop)


def items_category_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)


pre_save.connect(items_category_pre_save_receiver,sender=Item)


def category_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver,sender=Category)



def subcategory_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)


pre_save.connect(subcategory_pre_save_receiver,sender=SubCategory)

'''''
def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver,sender=Product)

'''



class Feedback(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    sub= models.CharField(max_length=300)
    feedback = models.CharField(max_length=1000)

    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
