from django.forms import ModelForm
from .models import Product

class UpdateProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','image']