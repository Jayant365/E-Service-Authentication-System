from django.contrib.auth.models import User
from django import forms
from .models import Feedback


#hair i wil do a shortcut that can be cahged furthere acccordign to need here iwill change quantity to one,

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 50)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class Feedbackform(forms.ModelForm):
    feedbacks = forms.CharField(widget=forms.Textarea, label="enter the feedback:")

    class Meta:
        model = Feedback

        fields = ['email', 'feedbacks']
