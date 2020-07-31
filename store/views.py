from django.shortcuts import render
from .models import Product
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

# Create your views here.
# cart_id = request.session.get('cart_id', None)


def home(request):
    product = Product.objects.all().order_by('date_created')
    query = request.GET.get('q')
    if query:
        product = product.filter(
            name__icontains=query
        ).distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(product, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    contexts = {'products': products}
    return render(request, 'store/home.html', contexts)


