from django.shortcuts import render, redirect, HttpResponseRedirect

from store.models.product import Products
from store.models.category import Category
from store.models.product_inventory import ProductInventory

from django.views import View


# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        out_of_stock = request.session.get('out_of_stock')

        if cart:
            quantity = cart.get(product)
            if quantity:
                cart, request, render_val = self.add_or_remove_cart_items(quantity, product, cart, request, out_of_stock)
                if render_val:
                    return redirect('homepage')
            else:
                cart[product] = 1
                out_of_stock[product] = False
        else:
            cart = {product: 1}
            out_of_stock[product] = False

        request.session['cart'] = cart
        request.session['out_of_stock'] = out_of_stock
        print('cart', request.session['cart'])
        return redirect('homepage')

    @staticmethod
    def get(request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

    @staticmethod
    def is_product_available(product_id, quantity):
        inventory_obj = ProductInventory.get_inventory_count(product_id)
        if quantity <= inventory_obj.product_quantity:
            if quantity < inventory_obj.max_count_to_cart:
                return True
            else:
                return False
        else:
            return False

    def add_or_remove_cart_items(self, quantity, product, cart, request, out_of_stock):
        render_val = False
        if request.POST.get('remove'):
            if quantity <= 1:
                cart.pop(product)
            else:
                cart[product] = quantity - 1
                out_of_stock[product] = False
        else:
            if self.is_product_available(product, quantity):
                cart[product] = quantity + 1
            else:
                request.session['cart'] = cart
                out_of_stock[product] = True
                request.session['out_of_stock'] = out_of_stock
                cart[product] = quantity + 1
                render_val = True
        return cart, request, render_val


def store(request):
    cart = request.session.get('cart')
    out_of_stock = request.session.get('out_of_stock')
    if not cart:
        request.session['cart'] = {}
        request.session['out_of_stock'] = {}
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        products = Products.get_all_products_by_category_id(category_id)
    else:
        products = Products.get_all_products()

    data = {'products': products, 'categories': categories}

    print('You are logged in with email : ', request.session.get('email'))
    return render(request, 'html/index.html', data)

