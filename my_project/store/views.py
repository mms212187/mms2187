from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):

    query = request.GET.get('q')
    if query:

        products = Product.objects.filter(name__icontains=query)
    else:

        products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products, 'query': query})

def product_detail(request, pk):

    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def add_product(request):
    """Добавление нового товара."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})
