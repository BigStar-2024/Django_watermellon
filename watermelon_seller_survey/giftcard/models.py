from djmoney.models.fields import MoneyField
from django.db import models


class GiftCard(models.Model):
    survey_id = models.CharField(max_length=50, blank=True)
    store_name = models.CharField(max_length=200, null=True, blank=True)
    number = models.IntegerField(default=0, null=True, blank=True)
    pin = models.CharField(max_length=20)

    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True)

    accepts_crypto = models.BooleanField(null=True)

    ETHEREUM = 'ethereum'
    POLYGON = 'polygon'
    CRYPTO_NETWORK_CHOICES = [
        (ETHEREUM, 'Ethereum eth.'),
        (POLYGON, 'Polygon Matic'),
    ]
    crypto_network = models.CharField(
        max_length=20,
        choices=CRYPTO_NETWORK_CHOICES,
        default=None, blank=True, null=True
    )

    wallet_address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    DEPOSIT_CHOICES = [
        ('deposit', 'deposit'),
        ('validate', 'validate'),
    ]
    deposit_or_validate  = models.CharField(
        max_length=20,
        choices=DEPOSIT_CHOICES,
        default=None, blank=True, null=True
    )

    deposit_confirm = models.BooleanField(default=None, null=True)

