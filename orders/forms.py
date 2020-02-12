
from django import forms
from .models import Order

area = [
    ('','Select'),
    ('Narender nagar', 'Narender nagar'),
    ('Sector 1A', 'Sector 1'),
    ('Roop nagar', 'Roop nagar'),
    ('patel nagar', 'Patel nagar'),
]


class OrderCreateForm(forms.ModelForm):
   # s_area = forms.CharField(label='Select your local area:', widget=forms.Select(choices=area),initial=None)

    class Meta:
        model = Order
        fields = ['phone_no', 'addr','date','timing','num']
