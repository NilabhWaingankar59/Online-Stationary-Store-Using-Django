from accounts.models import category, customer, products
from django.shortcuts import render
from templates import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import auth

def home(request):
    product=products.objects.all()
    catogerys=category.objects.all()
    return render(request, 'index.html',{'product':product , 'cat':catogerys})


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def customersignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        district = request.POST['district']
        pin = request.POST['pin']
        password = request.POST['password']
        repass = request.POST['re_password']
        if password == repass:
            if User.objects.filter(email=email).exists():
                print('email')
                # mess = "Email is already taken."
                # return render(request, 'stusignup.html', {'mess': mess})
            else:
                user = User.objects.create_user(email=email,username=email,
                                                first_name=fname,last_name=lname, password=password)
                suser = customer(contact=contact,address=address,district=district,pin=pin, user=user)
                suser.save()
                print("success")
                return redirect('/signin')
        else:
            mess = "Password is incorrect."
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def customersignin(request):
    print(request.method)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        if User.objects.filter(email=email).exists():
            user = auth.authenticate(username=email, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                mess = "Invalid Credentials."
                return render(request, 'stusignin.html', {'mess': mess})
        else:
            mess = "Invalid Credentials."
            return render(request, 'stusignin.html', {'mess': mess})
    else:
        return render(request, 'stusignin.html')

def productsView(request,catid):
    product=products.objects.all().filter(catid_id=catid)
    print(product[0].name)
    return render(request,'products.html',{'product': product})


def logout(request):
    auth.logout(request)
    return redirect('/')
