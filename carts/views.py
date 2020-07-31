from django.shortcuts import get_object_or_404, HttpResponse, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from carts.models import Cart, CartItems, Payment, Refund
from django.contrib.auth.models import User
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from carts.forms import BillingAddressForm, RefundForm
from paystack.resource import TransactionResource
from django.conf import settings
import random
import string


@login_required
def order_summary(request):
    try:
        request.session.set_expiry(43200)
        carts = Cart.objects.get(user=request.user, ordered=False)
        return render(request, 'carts/cart.html', {'carts': carts})
    except ObjectDoesNotExist:
        messages.error(request, 'You do not have an active order.')
        return redirect("store:home")


@login_required
def add_to_cart(request, slug):
    cart_id = request.session.get('cart_id', None)
    item = get_object_or_404(Product, slug=slug)
    cart_item, created = CartItems.objects.get_or_create(items=item,
                                                         user=request.user,
                                                         ordered=False)
    cart_qs = Cart.objects.filter(id=cart_id, user=request.user, ordered=False)
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
        request.session['cart_id'] = order.id
        # print(order.id)
        messages.success(request, 'Your order item has been updated.')
        return redirect("store:home")


@login_required
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


@login_required
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


@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user, ordered=False)
        if request.method == 'POST':
            form = BillingAddressForm(request.POST)
            if form.is_valid():
                billing_address = form.save()
                cart.billing_address = billing_address
                cart.save()
                return redirect('carts:pay')
            else:
                messages.error(request, 'You cannot submit the form without filling all the form fields appropriately')
        else:
            form = BillingAddressForm()
        carts = Cart.objects.get(user=request.user, ordered=False)
        return render(request, 'carts/checkout.html', {'carts': carts, 'form': form})
    except ObjectDoesNotExist:
        messages.info(request, 'No active order')
        return redirect('carts:checkout')


@login_required
def pay(request):
    carts = Cart.objects.get(user=request.user, ordered=False)
    rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
    secret_key = settings.API_SECRET_KEY
    reference = rand
    test_email = request.user.email
    test_amount = int(carts.cart_total_price()*100)
    client = TransactionResource(secret_key, reference)
    response = client.initialize(test_amount, test_email)
    authorization_url = response['data']['authorization_url']
    print(response)
    # authorization = client.authorize()

    # create payment object
    payment = Payment()
    payment.amount = test_amount
    payment.user = request.user
    payment.save()

    # ASSIGN PAYMENT TO THE ORDER
    cart_items = carts.items.all()
    cart_items.update(ordered=True)
    for items in cart_items:
        items.save()
    carts.ordered = True
    carts.payment = payment
    carts.reference = reference
    carts.save()
    return redirect(authorization_url)


@login_required
def request_refund(request):
    if request.method == 'POST':
        form = RefundForm(request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            # Get the Cart/Order
            try:
                cart = Cart.objects.get(reference=ref_code)
                cart.request_refund = True
                cart.save()
                # STORE THE REFUND
                refund = Refund()
                refund.cart = cart
                refund.reason = message
                refund.save()
                messages.info(request, 'Your request was received')
                return redirect('carts:refund')
            except ObjectDoesNotExist:
                messages.info(request, 'This order does not exist.')
                return redirect('carts:refund')
        else:
            messages.info(request, 'This order does not exist.')
            return redirect('carts:refund')

    else:
        form = RefundForm()
        return render(request, 'carts/request-refund.html', {'form': form})




