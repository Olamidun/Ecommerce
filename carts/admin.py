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


admin.site.site_header = 'Estore Admin Dashboard'
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems)
admin.site.register(BillingAddress)
admin.site.register(Payment)
admin.site.register(Refund)





# from inspect import getmodule
# import django.contrib.admin.sites
# from django.http import Http404
# import logging
#
# logger = logging.getLogger(__name__)
#
#
# class RestrictStaffToAdminMiddleware:
#     """
#     A middleware that restricts staff members access to administration panels.
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         module = getmodule(view_func)
#         if (module is django.contrib.admin.sites) and (not request.user.is_staff):
#             ip = request.META.get('HTTP_X_REAL_IP', request.META.get('REMOTE_ADDR'))
#             ua = request.META.get('HTTP_USER_AGENT')
#             logger.warn(f'Non-staff user "{request.user}" attempted to access admin site at "{request.get_full_path()}". UA = "{ua}", IP = "{ip}", Method = {request.method}')
#             raise Http404

