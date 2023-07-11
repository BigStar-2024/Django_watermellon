from django import forms
from .models import GiftCard
from djmoney.forms.widgets import MoneyWidget

from django.forms.widgets import Select


class BootstrapSelect(Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
        self.attrs.update({'class': 'form-select'})


class GiftCardForm(forms.ModelForm):
    class Meta:
        model = GiftCard
        fields = ['store_name', 'amount', 'crypto_network',
                  'wallet_address', 'deposit_or_validate', 'deposit_confirm', 'email']
        widgets = {
            'amount': MoneyWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter amount'
                },
                # amount_widget_attrs={
                #     'class': 'form-control',
                #     'placeholder': 'Enter amount'
                # }
            ),
            'crypto_network': BootstrapSelect(),
            'deposit_or_validate': BootstrapSelect(),
        }
