from django.db import models
from store.models import Product
from django.contrib.auth.models import User


class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True, blank=True)
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    line_total = models.FloatField(null=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.items.name}"

    def cart_item_price(self):
        if self.items.discount_price:
            return self.quantity * self.items.discount_price
        else:
            return self.quantity * self.items.price


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(CartItems, null=True, blank=True, related_name='item_cart')
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)
    request_refund = models.BooleanField(default=False)
    granted = models.BooleanField(default=False)
    reference = models.CharField(max_length=16, blank=True, null=True)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def cart_total_price(self):
        total = 0.00
        for cart_item in self.items.all():
            total += cart_item.cart_item_price()
        return total


# payment_choices = (
#     ('s', 'stripe'),
#     ('p', 'paypal'),
#     ('c', 'credit card')
# )

class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=255)
    apartment_address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    # payment_options = models.Choices(payment_choices)

    def __str__(self):
        return self.address


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField(null=True, blank=True)

    time_stamp = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s payment of {self.amount}"


class Refund(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}'
