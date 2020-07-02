from django.urls import path
from carts import views

app_name = 'carts'

urlpatterns = [
    path('order-summary', views.order_summary, name='order_summary'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('reduce-quantity/<slug:slug>/', views.reduce_quantity_of_items, name='reduce_quantity'),
    path('checkout/',  views.checkout, name='checkout'),
    path('pay-with-paystack/', views.payment, name='pay')
]
