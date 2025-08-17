from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from catalog.models import Product
from decimal import Decimal

CART_SESSION_KEY = "cart"   # { product_id: qty }

def _get_cart(session):
    return session.setdefault(CART_SESSION_KEY, {})

def add_to_cart(request, product_id):
    cart = _get_cart(request.session)
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    request.session.modified = True
    return redirect(reverse("cart_detail"))

def increment_item(request, product_id):
    cart = _get_cart(request.session)
    pid = str(product_id)
    if pid in cart:
        cart[pid] += 1
        request.session.modified = True
    return redirect(reverse("cart_detail"))

def decrement_item(request, product_id):
    cart = _get_cart(request.session)
    pid = str(product_id)
    if pid in cart:
        cart[pid] -= 1
        if cart[pid] <= 0:
            del cart[pid]
        request.session.modified = True
    return redirect(reverse("cart_detail"))

def remove_from_cart(request, product_id):
    cart = _get_cart(request.session)
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
        request.session.modified = True
    return redirect(reverse("cart_detail"))

def cart_detail(request):
    cart = _get_cart(request.session)
    items = []
    total = Decimal("0.00")
    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=int(pid))
        line_total = product.price * qty
        total += line_total
        items.append({
            "product": product,
            "qty": qty,
            "line_total": line_total,
        })
    return render(request, "cart/cart_detail.html", {"items": items, "total": total})
