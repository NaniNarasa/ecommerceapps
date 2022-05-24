from django.shortcuts import render
from django.views import View


class AboutUsView(View):
    return_url = None

    @staticmethod
    def get(request):
        AboutUsView.return_url = request.GET.get('return_url')
        return render(request, 'html/about_us.html')
