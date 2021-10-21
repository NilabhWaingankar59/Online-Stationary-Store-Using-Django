from accounts.models import cartproduct, category, customer, products,cart,order,orderproduct
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

def carts(request):
    customerid = request.user.id
    cartid = (cart.objects.all().filter(custid_id=customerid))[0]
    cp=cartproduct.objects.all().filter(cartid=cartid)
    product=products.objects.all() 
    if cart.objects.all().filter(custid_id=request.user.id).exists()==False:
        c = cart(custid_id=request.user.id)
        c.save()
        print("success")
    return render(request,'cart.html',{'cp':cp,'product':product})

def logout(request):
    auth.logout(request)
    return redirect('/')

def itemadded(request,pid):
    customerid=request.user.id
    p=products.objects.all().filter(id=pid)[0]
    cartid=(cart.objects.all().filter(custid_id=customerid))[0]
    if request.method == 'GET' and cartproduct.objects.filter(pid=pid).exists()==False:
        i=cartproduct(cartid=cartid,pid=p,n=3)
        i.save()
        print("success")

    return redirect("/")

def updatecart(request):
    a = request.POST.getlist("nof")
    id=request.POST.getlist("productid")
    print(a)
    print(id)
    for idx, i in zip(id,a):
        t=cartproduct.objects.get(id=int(idx))
        print(t)
        t.n=i
        t.save()
        print("sucess")

    return redirect('/cart')

def removeitem(request,pid):
    cartproduct.objects.filter(pid_id=pid).delete()
    print(pid,"dsss")
    return redirect("/cart")

def checkout(request):
    customerid = request.user.id
    print(customerid)
    cust = (customer.objects.all().filter(user_id=customerid))[0]
    cartid = (cart.objects.all().filter(custid_id=customerid))[0]
    cp = cartproduct.objects.all().filter(cartid=cartid)
    product = products.objects.all()
    if request.method == 'POST':
        return redirect("/")
    return render(request, 'order.html', {'cp': cp, 'product': product, 'cust':cust})

def yourorder(request,oid=0):
    print(oid)
    customerid = request.user.id
    cust = (customer.objects.all().filter(user_id=customerid))[0]
    cartid = (cart.objects.all().filter(custid_id=customerid))[0]
    cp = cartproduct.objects.all().filter(cartid=cartid)
    product = products.objects.all()
    if request.method=='POST':
        paymenttype = request.POST.get('imp')
        print(paymenttype)
        i = order(custid=request.user, paymenttype=paymenttype)
        i.save()
        print("SUCESSSSSSSSSSSSSSSSSSS")
        for j in cp:
            k=orderproduct(orderid=i,pid=j.pid,n=j.n)
            k.save()
        cp.delete()
        print("Sucess")
        cp = orderproduct.objects.all().filter(orderid=i.id)
    else:
        cp = orderproduct.objects.all().filter(orderid=oid)
    return render(request, 'placedorder.html', {'cp':cp, 'product': product,'cust':cust})

def orderlist(request):
    customerid = request.user.id
    order1 = order.objects.all().filter(custid_id=customerid)
    return render(request, 'orderlist.html', {'order': order1})

