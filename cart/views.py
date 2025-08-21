from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from decimal import Decimal


def _get_cart(request):
    return request.session.setdefault("cart", {})

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
    cart = request.session.get("cart", {})
    items = []
    total = Decimal("0.00")

    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=int(pid_str))
        line_total = product.price * qty
        total += line_total
        items.append({
            "product": product,
            "qty": qty,
            "line_total": line_total,
        })

    return render(request, "cart/cart_detail.html", {"cart_items": items, "cart_total": total})

@require_POST
def add_to_cart(request, product_id):
    cart = _get_cart(request)
    qty = int(request.POST.get("quantity", 1))
    key = str(product_id)
    cart[key] = cart.get(key, 0) + qty
    request.session.modified = True
    return redirect("cart:detail")

@require_POST
def add_to_cart(request, product_id):
    cart = _get_cart(request)
    qty = int(request.POST.get("quantity", 1))
    key = str(product_id)
    cart[key] = cart.get(key, 0) + qty
    request.session.modified = True
    return redirect("cart:detail")

@require_POST
def remove_from_cart(request, product_id):
    cart = _get_cart(request)
    cart.pop(str(product_id), None)
    request.session.modified = True
    return redirect("cart:detail")

@require_POST
def clear_cart(request):
    request.session["cart"] = {}
    request.session.modified = True
    return redirect("cart:detail")