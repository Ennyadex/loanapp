from django.shortcuts import render
from .models import Customer
from .models import Register
from random import randint
from .models import Login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone_number =request.POST['phone_number']
        gender = request.POST['gender']
        state = request.POST['state']
        
        form = Customer(name=name,address=address,phone_number=phone_number,gender=gender,state=state)
        form.save()
        
        
    return render(request, 'customer.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        country = request.POST['country']
        password = request.POST['password']
        unique_no = randints(10)
        
        form2 = Register(username=username,email=email,country=country,password=password,unique_no=unique_no)
        form2.save()
        
    return render(request,'register.html')


def randints(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        form3 = Login(email=email,password=password)
        form3.save()
        
    return render(request,'login.html')