from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/details', views.product_details, name="details")
]
