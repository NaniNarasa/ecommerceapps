from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render

from store.models.customer import Customer
from store.models.product import Products
from store.models.orders import Order
from store.models.address import Address


class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        order_list = []
        order_id = self.get_max_order_id()
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(order_id=order_id,
                          customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()

        request.session['orders_id'] = order_id
        print(order_list)
        request.session['cart'] = {}
        request.session['order_status'] = True
        print(request.session.get('order_status'))

        return redirect('cart')

    @staticmethod
    def get_max_order_id():
        order = Order.get_max_order_id()
        if len(order) == 0:
            return 1000
        else:
            return order.order_id+1

    @staticmethod
    def customer_addresses(request):
        customer = request.session.get('customer')
        print("Printing customer id : " + str(customer))
        address_list = Address.get_addresses_by_customer(customer)
        print(address_list)
        return render(request, "cart.html", {"address_list": address_list})
