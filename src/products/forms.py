from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="Your title")
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'size': '40',
            'placeholder': 'Your description'}
    )
    )
    price = forms.DecimalField(initial=199)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "cfe" in title.lower():
            raise forms.ValidationError("Not valid title")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label="Your title")
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'size': '40',
            'placeholder': 'Your description'}
    )
    )
    price = forms.DecimalField(initial=199)
