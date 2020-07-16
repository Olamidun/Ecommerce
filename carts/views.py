from django.shortcuts import get_object_or_404, HttpResponse, redirect, render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from carts.models import Cart, CartItems, Payment
from django.contrib.auth.models import User
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from carts.forms import BillingAddressForm, PaymentForm
import requests


@login_required
def order_summary(request):
    try:
        carts = Cart.objects.get(user=request.user, ordered=False)
        return render(request, 'carts/cart.html', {'carts': carts})
    except ObjectDoesNotExist:
        messages.error(request, 'You do not have an active order.')
        return redirect("store:home")


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_item, created = CartItems.objects.get_or_create(items=item,
                                                         user=request.user,
                                                         ordered=False)
    cart_qs = Cart.objects.filter(user=request.user, ordered=False)
    if cart_qs.exists():
        order = cart_qs[0]
        if order.items.filter(items__slug=item.slug).exists():
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, 'Your order item has been updated.')
            return redirect("carts:order_summary")
        else:
            order.items.add(cart_item)
            messages.info(request, 'Your Item has been added to cart successfully!')
            return redirect("store:home")
    else:
        order = Cart.objects.create(user=request.user, created_on=timezone.now())
        order.items.add(cart_item)
        messages.success(request, 'Your order item has been updated.')
        return redirect("store:home")


def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, ordered=False)
    if cart_qs.exists():
        order = cart_qs[0]
        if order.items.filter(items__slug=item.slug).exists():
            cart_item = CartItems.objects.filter(items=item,
                                                 user=request.user,
                                                 ordered=False)[0]

            order.items.remove(cart_item)
            cart_item.delete()
            messages.info(request, 'This item has been removed from your cart.')
            return redirect("carts:order_summary")
        else:
            messages.info(request, 'This item is not in your cart.')
            return redirect("store:home")
    else:
        messages.error(request, 'You do not have an active order.')
        return redirect("carts:order_summary")


def reduce_quantity_of_items(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, ordered=False)
    if cart_qs.exists():
        order = cart_qs[0]
        if order.items.filter(items__slug=item.slug).exists():
            cart_item = CartItems.objects.get(items=item,
                                              user=request.user,
                                              ordered=False)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                order.items.remove(cart_item)
            messages.info(request, 'The quantity of this item was updated.')
            return redirect("carts:order_summary")
        else:
            messages.info(request, 'This item is not in the cart.')
            return redirect("store:home")
    else:
        messages.info(request, 'You do not have an active order.')
        return redirect("carts:order_summary")


def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user, ordered=False)
        if request.method == 'POST':
            forms = BillingAddressForm(request.POST)
            if forms.is_valid():
                billing_address = forms.save()
                cart.billing_address = billing_address
                cart.save()
                return redirect('carts:pay')
            else:
                messages.error(request, 'You cannot submit the form without filling all the form fields appropriately')
        else:
            forms = BillingAddressForm()
        carts = Cart.objects.get(user=request.user, ordered=False)
        return render(request, 'carts/checkout.html', {'carts': carts, 'forms': forms})
    except ObjectDoesNotExist:
        messages.info(request, 'No active order')
        return redirect('carts:checkout')


def payment(request):
    carts = Cart.objects.get(user=request.user, ordered=False)

    headers = {
        "Authorization": "Bearer sk_test_b17ddd192493898c2ceb258eebbe02771cb4aaa9",
        "Content-Type": "application/json"
    }
    data = {
        "email": "kolapoolamidun@gmail.com",
        "amount": "20000"
    }

    url = 'https://api.paystack.co/transaction/initialize'
    response = requests.post(url, headers=headers, data=data)
    response.json()
    print(response.status_code)
    return HttpResponse(response)




