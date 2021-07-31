from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
        postData = request.POST
        fname = postData.get('fname')
        lname = postData.get('lname')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')

        # validation

        values = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'phone': phone,
        }

        # saving

        customer = Customer(fname=fname, lname=lname, email=email, phone=phone, password=password)
        error_message = self.validateCustomer(customer)
        if not error_message:
            print(f"fname:{fname}, lname:{lname},email:{email},phone:{phone},Pass:{password}")
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('store')
            # customer.save()

        else:
            data = {
                'error': error_message,
                'value': values,

            }
            return render(request, 'store/signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if (not customer.fname):
            error_message = "First Name is Requird !!"
        elif len(customer.fname) < 2:
            error_message = "First Name Must be grater then 3 charecters !!"

        elif (not customer.lname):
            error_message = "last Name is Requird !!"
        elif len(customer.lname) < 3:
            error_message = "last Name Must be grater then 3 charecters !!"

        elif (not customer.email):
            error_message = "last Name is Requird !!"

        elif (not customer.phone):
            error_message = "Phone Number is Requird !!"
        elif len(customer.phone) < 11:
            error_message = "Phone Number Must be 11-15 charecters !!"

        elif (not customer.password):
            error_message = "Password is Requird !!"
        elif len(customer.password) < 8:
            error_message = "Password Must be grater then or equal 8 charecters !!"


        elif customer.isExists():
            error_message = "E-mail address already registered... !!"

        return error_message
