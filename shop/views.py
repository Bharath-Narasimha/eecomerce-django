from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.http import require_POST

# Dummy product data
PRODUCTS = [
    {'id': 1, 'name': 'T-shirt', 'description': 'Comfortable cotton t-shirt', 'price': 15.99, 'image': 'tshirt.jpg'},
    {'id': 2, 'name': 'Jeans', 'description': 'Stylish blue jeans', 'price': 39.99, 'image': 'jeans.jpg'},
    {'id': 3, 'name': 'Sneakers', 'description': 'Running sneakers', 'price': 59.99, 'image': 'sneakers.jpg'},
    {'id': 4, 'name': 'Jacket', 'description': 'Warm winter jacket', 'price': 89.99, 'image': 'jacket.jpg'},
]

def product_list(request):
    return render(request, 'shop/product_list.html', {'products': PRODUCTS})

def product_detail(request, product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        raise Http404('Product not found')
    return render(request, 'shop/product_detail.html', {'product': product})

@require_POST
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart_summary')

@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_summary')

def cart_summary(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for pid, qty in cart.items():
        product = next((p for p in PRODUCTS if p['id'] == int(pid)), None)
        if product:
            item_total = product['price'] * qty
            total += item_total
            cart_items.append({'product': product, 'quantity': qty, 'item_total': item_total})
    return render(request, 'shop/cart_summary.html', {'cart_items': cart_items, 'total': total})
