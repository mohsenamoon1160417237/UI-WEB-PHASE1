import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from shop.models import ProductCategory, ProductItem, ShoppingCard
from gallery.models import ProductGallery, HomeGallery


def product_detail(request, pk: int):
    if request.method == "POST":
        pass
    else:
        product = ProductItem.objects.get(id=pk)
        colors = product.colors
        in_stock = product.stock_count != 0
        images = ProductGallery.objects.filter(product=product)
        additional_info = product.additional_info
        related_products = ProductItem.objects.filter(
            category__id=product.category.id
        ).exclude(id=product.id)

        authenticated = request.user.is_authenticated
        if authenticated:
            cards = ShoppingCard.objects.filter(user=request.user)
            if cards.exists():
                card = cards.first()
            else:
                card = None
        else:
            card = None
        total_price = 0 if card is None else sum([x.get("price") * x.get("quantity") for x in card.products_storage])
        total_price = round(total_price, 2)
        return render(request, "ProductA.html", {
            'product': product,
            'colors': colors,
            'in_stock': in_stock,
            'images': images,
            'additional_info': additional_info,
            'related_products': related_products,
            'card': card,
            'authenticated': authenticated,
            'total_price': total_price
        })


def home(request):
    context = {
        'categories': ProductCategory.objects.values('name', 'image'),
        'image1': HomeGallery.objects.filter(index=1).first(),
        'image2': HomeGallery.objects.filter(index=2).first()
    }
    return render(request, context=context, template_name='index.html')


@login_required
def add_to_card(request):
    user = request.user

    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        id = data.get('id')
        quantity = data.get('quantity')
        price = float(data.get('price'))
        name = data.get('name')
        url = data.get('url')
        cards = ShoppingCard.objects.filter(user=user)
        if not cards.exists():
            ShoppingCard.objects.create(user=user,
                                        products_storage=[
                                            {'id': id,
                                             'quantity': quantity,
                                             'price': price,
                                             'name': name,
                                             'url': url}
                                        ])
        else:
            card = cards.first()
            products_storage = card.products_storage
            ids = [x.get('id') for x in products_storage]
            if id in ids:
                products_storage[ids.index(id)]['quantity'] += quantity
            else:
                products_storage.append({'id': id,
                                         'quantity': quantity,
                                         'price': price,
                                         'name': name,
                                         'url': url})
            card.products_storage = products_storage
            card.save(update_fields=['products_storage'])

        return redirect("home")


@login_required
def delete_from_card(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        id = data.get('id')
        card = ShoppingCard.objects.get(user=request.user)
        products_storage = card.products_storage
        ids = [x.get('id') for x in products_storage]
        del products_storage[ids.index(id)]
        card.products_storage = products_storage
        card.save(update_fields=['products_storage'])
        return redirect("home")
