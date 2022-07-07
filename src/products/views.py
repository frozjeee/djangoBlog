from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.


# def product_create_view(request):
#
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#             return redirect('/create/')
#         else:
#             print(my_form.errors)
#     else:
#         my_form = RawProductForm()
#     context = {
#         "form": my_form,
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/create/')
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.all()
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    # }
    context = {
        "querySet": obj,
    }
    return render(request, "products/product_detail.html", context)


# def render_initial_data(request):
#     initial_data = {
#         "title": "Awesome title"
#     }
#     obj = Product.objects.get(id=1)
#     form = ProductForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/create/')
#     context = {
#         "form": form
#     }
#     return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "obj": obj
    }
    return render(request, "products/product_dynamic.html", context)


def delete_product_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('/products/')
    context = {
        "obj": obj
    }
    return render(request, "products/product_delete.html", context)


def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/products/')
    context = {
        "form": form,
        "obj": obj
    }
    return render(request, "products/product_update.html", context)