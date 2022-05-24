from django.shortcuts import render
from django.views import View
from store.models import ContactUs


class ContactUsView(View):
    return_url = None

    @staticmethod
    def get(request):
        ContactUsView.return_url = request.GET.get('return_url')
        return render(request, 'html/contact_us.html')

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get('firstname')
        last_name = post_data.get('lastname')
        email = post_data.get('email')
        message = post_data.get('message')
        subscribe = 'YES' if post_data.get('subscribe') == 'true' else "NO"

        contact_us = ContactUs(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message,
            subscribe=subscribe)

        contact_us.register()

        return render(request, 'html/contact_us_response.html', {"contact_us": contact_us})


