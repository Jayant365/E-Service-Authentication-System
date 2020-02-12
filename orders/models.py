from django.db import models
from service.models import Product,Shop
from django.contrib.auth import get_user_model

User = get_user_model()



class Order(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    o_id=models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    addr = models.CharField(max_length=760)
    phone_no = models.CharField(max_length=11)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)
    num= models.IntegerField()
    date=models.DateField()
    timing=models.CharField(max_length=60)

    total_a_cost=models.DecimalField(max_digits=15, default=22,decimal_places=2)
    total_cost=models.DecimalField(max_digits=15, default=22,decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_i_price=models.DecimalField(max_digits=15, decimal_places=2)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class OrderDis(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    total_dis = models.DecimalField(max_digits=10, decimal_places=2)#before price
    total_saved_rs = models.DecimalField(max_digits=10, decimal_places=2)#total aved rs in a order
    extra_dis=models.DecimalField(max_digits=15, decimal_places=2)


    def __str__(self):
        return '{}'.format(self.id)


