from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        # когда нужно определенные поля, то используем массив fields = ['date_publication', 'status']
        fields = '__all__'
