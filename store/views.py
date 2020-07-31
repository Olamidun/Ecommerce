from django.shortcuts import get_object_or_404, render
from .models import Product
from django.contrib.auth.decorators import login_required
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


@login_required
def product_details(request, slug):
    item = get_object_or_404(Product, slug=slug)
    context = {'item': item}
    return render(request, 'store/items-details.html', context)


