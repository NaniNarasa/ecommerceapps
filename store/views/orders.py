from django.shortcuts import render
from django.views import View
from store.models.orders import Order


class OrderView(View):

    @staticmethod
    def get(request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'html/orders.html', {'orders': orders})
