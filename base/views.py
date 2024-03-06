from django.shortcuts import render, redirect
from .models import Customer
from .models import Register
from random import randint
from .models import Login
from .models import Status

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
        guarantor_name = request.POST['guarantor_name']
        g_number = request.POST['g_number']
        g_address = request.POST['g_address']
        loan_offer = request.POST['loan_offer']
        
        
        form = Customer(name=name,address=address,phone_number=phone_number,gender=gender,state=state,guarantor_name=guarantor_name,g_number=g_number,g_address=g_address,loan_offer=loan_offer)
        form.save()
        cus_status = Status(id=None,status="Pending",customer=form)
        cus_status.save()
        
        
    return render(request, 'customer.html')


def allcustomers(request):
       
       customers = Customer.objects.fil
       return render(request,'allcustomers.html',{'customers':customers})
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        country = request.POST['country']
        passwd = request.POST['passwd']
        unique_no = randints(10)
        
        form2 = Register(username=username,email=email,country=country,passwd=passwd,unique_no=unique_no)
        form2.save()
    
        return redirect('login')
        
    return render(request,'register.html')


def randints(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['passwd']
        
        form3 = Login(email=email,passwd=passwd)
        if form3.is_valid():
            form3.save()
            return redirect('dashbord')
        
    return render(request,'login.html')


def appadmin(request):
    
    
    return render(request,'admin.html')

def status(request):
    stat = Customer.objects.all
    if request.method == 'POST':
        stat = Status(request.POST)
        if stat.is_valid():
            stat.save()
            return redirect('dashbord')
    
    
    return render(request,'status.html',{'customers':stat})

def editstatus(request, pk):
    status = Status.objects.get(id=pk)
    editstatus = Status(instance=status)
    if request.method == 'POST':
        editstatus = Status(request.POST, instance = status)
        if editstatus.is_valid():
            editstatus.save()
            return redirect('allcustomers')
    
    return render(request,'status.html')