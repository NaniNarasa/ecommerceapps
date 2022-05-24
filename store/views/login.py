from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None

    @staticmethod
    def get(request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'html/login.html')

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['customer_name'] = customer.first_name+"..!"
                request.session['email'] = customer.email

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print(email, password)
        return render(request, 'html/login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
