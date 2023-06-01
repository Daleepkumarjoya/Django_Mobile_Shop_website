from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from math import ceil
# Create your views here.
from .models import Product, Contact, OrderedBooked


def HomePage(request):
    All_Products = []
    catprods = Product.objects.values('catogery', 'id')
    cats = {item['catogery'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(catogery=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        All_Products.append([prod, range(1, nSlides), nSlides])
    Dict = {'All_Products': All_Products}
    return render(request, 'index.html', Dict)


def Home(request):
    All_Products = []
    catprods = Product.objects.values('catogery', 'id')
    cats = {item['catogery'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(catogery=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        All_Products.append([prod, range(1, nSlides), nSlides])
    Dict = {'All_Products': All_Products}


#     return render(request, 'index.html')


def searchMatch(query, item):
    if query in item.Desc.lower() or query in item.name.lower() or query in item.catogery.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    All_Products = []
    catprods = Product.objects.values('catogery', 'id')
    cats = {item['catogery'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(catogery=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            All_Products.append([prod, range(1, nSlides), nSlides])
    Dict = {'All_Products': All_Products}
    return render(request, 'index.html', Dict)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('Phone', '')
        desc = request.POST.get('help', '')
        contactC = Contact(name=name, email=email, phone=phone, desc=desc)
        contactC.save()
        messages.info(request, "Your Query Has Been Submitted Successfully")
    return render(request, 'contact.html')


def Productview(request, Proid):
    # fetching the products using the id
    product = Product.objects.filter(id=Proid)
    return render(request, 'prodview.html', {'product': product[0]})


def Placeorder(request):
    if request.method == 'POST':
        OrderName = request.POST.get('name', '')
        OrderEmail = request.POST.get('email', '')
        OrderPhone = request.POST.get('phone', '')
        OrderCity = request.POST.get('City', '')
        OrderState = request.POST.get('State', '')
        OrderAddress = request.POST.get('address', '')
        if OrderName and OrderEmail and OrderPhone and OrderState and OrderCity and OrderAddress is not None:
            forOrder = OrderedBooked(name=OrderName, email=OrderEmail, phone=OrderPhone, City=OrderCity,
                                     State=OrderState,
                                     address=OrderAddress)
            forOrder.save()
            messages.info(request, "Your Order Has been Submitted Successfully ")
        else:
            messages.info(request, "Please Fill All The Fields ")
    return render(request, 'order.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        Password = request.POST['Password']
        CP = request.POST['CP']
        if Password == CP:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User Name Already Exist")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "User Email Already Exist")
            else:
                user = User.objects.create_user(username=username, password=Password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "User Registered Successfully")
                return redirect('/LogIn')
        else:
            messages.info(request, "Password did Not Match")
            return redirect('/register')

    return render(request, 'register.html')


def LogIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['Password']
        user = auth.authenticate(username=username, password=Password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credential")
    return render(request, 'LogIn.html')


def LogOut(request):
    auth.logout(request)
    return redirect('/')
