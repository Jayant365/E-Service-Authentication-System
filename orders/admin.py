from django.contrib import admin
from .models import Order, OrderItem,OrderDis


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderDisInline(admin.TabularInline):
    model = OrderDis
    fields = ['name',"total_dis","total_saved_rs","extra_dis"]

admin.site.register(OrderItem)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'name',  'addr','phone_no','total_cost', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline,OrderDisInline]

admin.site.register(Order, OrderAdmin)
