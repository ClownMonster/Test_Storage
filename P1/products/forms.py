from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = [
            'title',
            'description',
            'price',
            'discount',
            'mail_id'

        ]


class RawProductForm(forms.Form):
    title = forms.CharField()
    description  =  forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':20}))
    price = forms.IntegerField()
    discount =  forms.DecimalField()
    mail_id = forms.EmailField()