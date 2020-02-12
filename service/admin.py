from django.contrib import admin
from .models import Product,Category,Feedback,Shop,Item,SubCategory,Facility


admin.site.register(Item)
admin.site.register(Facility)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Feedback)
#admin.site.register(UserForm)

# Register your models here.
# class ProductInline(admin.TabularInline):
#     model = Product
#     raw_id_fields = ['name']

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','name','updated_at']
    list_filter = ['category', 'created_at', 'updated_at']
  #  inlines = [ProductInline]

admin.site.register(Shop,ShopAdmin)

from django import forms
from django.contrib import admin

from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

#Create custom form with specific queryset:
class CustomBarModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomBarModelForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(worker=True)# or something else

# Use it in your modelAdmin
class ProductAdmin(admin.ModelAdmin):
    form = CustomBarModelForm

admin.site.register(Product,ProductAdmin)
