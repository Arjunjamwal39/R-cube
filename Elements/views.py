from cmath import log
from pdb import post_mortem
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from sympy import product
from .models import Cart, Customer, OrderStatus, Product, practice, UserOTP, Deliveryboy
from django.shortcuts import render
from .forms import Customerprofilee, EnterdaUser, Forgotpass, LogindaUser
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User 
#Create your views here.


class Homeyview(View):
    def get(self, request):
        sl = Product.objects.filter(category='L')
        slider = practice.objects.all()
        noofitems = 0
        if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
        return render(request, 'Homey.html', {'sl':sl, 'noofitems':noofitems,'slider':slider})

class Practiceview(View):
    def get(self, request):
        Crouu = Product.objects.filter(category='L')
        return render(request, 'practice.html', {'s':Crouu})

@method_decorator(login_required, name='dispatch')
class ItemDetailView(View):
    def get(self, request, pk):
        itemm = Product.objects.get(pk=pk)
        cart_have_item = False
        cart_have_item = Cart.objects.filter(Q(product=itemm.id) & Q(user=request.user)).exists()
        noofitems = 0
        if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
        return render(request, 'itemdetail.html', {'itemm':itemm,'cart_have_item': cart_have_item,'noofitems':noofitems})

def Productdisplay(request, data = None):
    noofitems = 0
    if data == None:
        showw = Product.objects.all()
    elif data == 'E' or data == 'C' or data == 'F' or data == 'H' or data == 'L':
        showw = Product.objects.filter(category=data)
        
        
    if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
    return render(request, 'allproduct.html', {'showw':showw, 'noofitems':noofitems})


def EnterdaUserplz(request):

    if request.method == 'POST':
        grab_otp = request.POST.get('otp')
        if grab_otp:
             grab_usrr = request.POST.get('usrr')
             usrr = User.objects.get(username = grab_usrr)
             if int(grab_otp) == UserOTP.objects.filter(user = usrr).last().otp:
                 messages.success(request, f'Account is created for {usrr.username}')
                 form = EnterdaUser()
                 return render(request, 'sin_up.html',{'form':form})
             else:
                 messages.error(request,f'You entered a wrong OTP')
                 return render(request, 'sin_up.html',{'otp':True,'usrr':usrr})   
        
        
        form = EnterdaUser(request.POST)
        if form.is_valid():
            #messages.success(request, 'Greetings !!! You are registered to the Rcube')
            form.save()
            username = form.cleaned_data.get('username')
            usrr = User.objects.get(username = username)
            customer_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usrr, otp = customer_otp)
            usrr.save()
            print('service 300')
            print(usrr)
            otp_message = f"Wlcome to Rcube\n\n\nHello {usrr.first_name},\n Your OTP is {customer_otp}\n\nYour username, in case you’ve forgotten: {usrr}\n\nthanks!"
            send_mail(
                "Welcome to RCUBE - Verify your Email",
                otp_message,
                settings.EMAIL_HOST_USER,
                [usrr.email],
                fail_silently=False
            )
            return render(request, 'sin_up.html', {'otp':True,'usrr':usrr})

    else:
        form = EnterdaUser()
    return render(request, 'sin_up.html',{'form':form})

def profile(request):
    print('db:- ',request.user)
    cu = request.user  #cathes username from db
    print('cu value:-',cu)
    user_id = cu.id
    print('name:- ', cu.first_name)
    print('this is user id:-', user_id)
    cont = {'user_id': user_id}
    print(cu.email)
    noofitems = 0
    if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
    return render(request, 'profile.html',{'noofitems':noofitems,'cont':cont})

@method_decorator(login_required, name='dispatch')
class Profileadd(View):
    def get(self, request):
        u = request.user
        print(u)
        form = Customerprofilee()
        noofitems = 0
        if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
        return render(request, 'Customerprofilee.html',{'form':form, 'acc':u, 'noofitems':noofitems})

    def post(self, request):
        form = Customerprofilee(request.POST)
        if form.is_valid():
            u = request.user
            name = form.cleaned_data['name']
            Contact_number = form.cleaned_data['Contact_number']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            add_type = form.cleaned_data['address_type']
            stamp = Customer(user=u, name= name, Contact_number=Contact_number,locality=locality, city = city, zipcode=zipcode,
            state = state, address_type = add_type)
            stamp.save() 
            messages.success(request,'Profile Updated Successfully')
        form = Customerprofilee()
        noofitems = 0
        if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
        return render(request, 'Customerprofilee.html', {'form':form, 'acc':form,'noofitems':noofitems})    



def showaddress(request):
    dis = Customer.objects.filter(user = request.user)
    noofitems = 0
    if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
    
    return render(request, 'useraddress.html', {'dis':dis,'noofitems':noofitems})

def showcart(request):
    user = request.user
    print(user)
    prodId = request.GET.get('prod_id')
    print(prodId)
    getprod = Product.objects.get(id = prodId)
    Cart(user=user , product = getprod).save()
    return redirect('/cart')

def displaycart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user = user)
        print(cart)
        amount = 0.0
        shipping = 120
        total = 0.0
        cart_item = [p for p in Cart.objects.all() if p.user == user]
        print(cart_item)
        noofitems = 0
        if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))

        if cart_item:
            for p in cart_item:
                temp = (p.quantity * p.product.price)
                amount += temp
                total = amount + shipping
                print('After shipping:-',total)
                print(amount)
            return render(request, 'add-to-cart.html',{'cart':cart, 'total':total, 'amount':amount,'noofitems':noofitems})
        else:
            return render(request, 'hollowcart.html')

def cart_add(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user)) #encapsulation
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping = 120
        cart_item = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_item:
            temp = (p.quantity * p.product.price)
            amount += temp
            
        data = {'quantity':c.quantity,'amount':amount,'total':amount + shipping}
        return JsonResponse(data)

def cart_subtract(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user)) #encapsulation
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping = 120
        cart_item = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_item:
            temp = (p.quantity * p.product.price)
            amount += temp
            
        data = {'quantity':c.quantity,'amount':amount,'total':amount + shipping,}
        return JsonResponse(data)

def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user)) #encapsulation
        c.quantity -= 1
        c.delete()
        amount = 0.0
        shipping = 120
        cart_item = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_item:
            temp = (p.quantity * p.product.price)
            amount += temp
            
        data = {'amount':amount,'total':amount + shipping}
        return JsonResponse(data)



def checkout(request):
    user =request.user
    add = Customer.objects.filter(user = user)
    cart_item = Cart.objects.filter(user = user)
    amount = 0.0 
    shipping = 120
    cart_prod = [p for p in Cart.objects.all() if p.user == request.user]
    noofitems = 0
    if request.user.is_authenticated:
            noofitems = len(Cart.objects.filter(user = request.user))
    if cart_prod:    
        for p in cart_prod:
            temp = (p.quantity * p.product.price)
            amount += temp
        total = amount + shipping
    return render(request, 'checkout.html', {'add':add, 'total':total, 'cart_item':cart_item,'noofitems':noofitems})
    
def paymentdone(request):
    user =request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id = custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderStatus(user=user, customer = customer, product = c.product, quantity = c.quantity).save()
        c.delete()
    return redirect("orders") 

@login_required
def orders(request):
    placed = OrderStatus.objects.filter(user = request.user)
    pl = Customer.objects.filter(user = request.user)
    for o in pl:
        w = o.name
        con = o.Contact_number
        loc = o.locality
        cit = o.city
        zipp = o.zipcode

        print(w) 
    valet = [p for p in Deliveryboy.objects.all() if p.stat == 'free']
    for p in valet:
        nn = p.Name
        cc = p.Contact_number
        dd = p.discription
        ee = p.emaill
        print(p.Name)
        break
    
    delivery_message = f"Wlcome to Rcube\n\n\nHello {nn},\n today delivery details:\n\n customer name: {w} \n\nContact:{con}\n\nAddress:{loc}, {cit},{zipp}\n\n\nthanks!"
    send_mail(
                "Welcome to RCUBE - Delivery Details",
                delivery_message,
                settings.EMAIL_HOST_USER,
                [ee],
                fail_silently=False
            )
    return render(request, 'orders.html', {'placed':placed,'dliname':nn,'dlicontact':cc})   

