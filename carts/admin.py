from django.contrib import admin
from carts.models import BillingAddress, Cart, CartItems, Payment
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'billing_address']
    list_display_links = ['billing_address']
    search_fields = ['user__username']


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems)
admin.site.register(BillingAddress)
admin.site.register(Payment)
