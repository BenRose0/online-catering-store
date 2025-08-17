from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    q = request.GET.get("q", "")
    cat = request.GET.get("cat", "")
    qs = Product.objects.all()
    if q:
        qs = qs.filter(name__icontains=q)
    if cat:
        qs = qs.filter(category__slug=cat)

    paginator = Paginator(qs.order_by("-created_at"), 12)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    categories = Category.objects.all()

    return render(
        request,
        "catalog/product_list.html",
        {"products": products, "categories": categories, "q": q, "cat": cat},
    )

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "catalog/product_detail.html", {"product": product})
