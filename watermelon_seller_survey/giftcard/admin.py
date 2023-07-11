from django.contrib import admin
from .models import GiftCard


@admin.register(GiftCard)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'survey_id',
        'store_name',
        'amount',
        'price',
        'accepts_crypto',
        'crypto_network',
        'wallet_address',
        'deposit_or_validate',
        'email')