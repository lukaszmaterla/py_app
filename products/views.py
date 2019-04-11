from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import Http404
from .forms import ProductForm


# def product_create_view(request):
#     print(request.POST)
#     context = {}
#     return render(request, 'products/product_create.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj,
    }
    return render(request, 'products/product_detail.html', context)


def product_lookup_view(request, pk):
    # obj = Product.objects.get(id=pk)
    # obj = get_object_or_404(Product, id=pk)
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404

    context = {
        'object': obj,
    }
    return render(request, 'products/product_detail.html', context)


def product_delete_view(request, pk):
    obj = get_object_or_404(Product, id=pk)
    # obj.delete()
    if request.POST == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)
