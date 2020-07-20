from django.contrib import admin
from carts.models import BillingAddress, Cart, CartItems, Payment, Refund
# Register your models here.


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(request_refund=False, granted=True)


make_refund_accepted.short_description = 'Grant Refund'


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'billing_address', 'request_refund', 'granted', 'payment']
    list_display_links = ['user', 'billing_address', 'payment']
    search_fields = ['user__username', 'reference']
    actions = [make_refund_accepted]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems)
admin.site.register(BillingAddress)
admin.site.register(Payment)
admin.site.register(Refund)

