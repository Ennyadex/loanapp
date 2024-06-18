from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Login
from .models import Customer
from .models import Register
from random import randint
from .models import Status
from .models import Applyloan
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput,EmailInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def home(request):
    allcustomers = Customer.objects.filter().count()
    approved =  Customer.objects.filter(status__status = 'Approved').count()
    pending = Customer.objects.filter(status__status = 'Pending').count()
    tloan = Customer.objects.aggregate(TOTAL = Sum('loan_offer')) ['TOTAL']

    return render(request, 'home.html',{'allcustomers':allcustomers,'approved':approved,'pending':pending,'tloan':tloan})

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


def editcustomers(request):
       
       customers = Customer.objects.prefetch_related('status_set').values_list('name','address','phone_number','gender','state','status__status','status__id','id','loan_offer')
       for x in customers:
           print(x)
          
       return render(request,'editcustomers.html',{'customers':customers})
    
def user_signup(request):
    if request.method == "POST":
       form = SignupForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')
       else:
           print("opps")
    
    messages.error(request,"errrrror")
    signupForm = SignupForm()
    return render(request, 'signup.html',{'forms': signupForm})


def randints(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
       
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            user = authenticate(request,username=username,password=password)
            if user is not  None:
                login(request,user)
                messages.info(request,f"You are logged in as {username}.")
                return redirect('dashboard')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password")
    form = LoginForm()
    return render(request,'login.html',{'form':form})


def loggedout(request):
    logout(request)
    messages.info(request, "you have successfully logged out. ")
    return redirect('login')

def appadmin(request):
    return render(request,'admin.html')

def viewstatus(request):
    stat = Customer.objects.prefetch_related('status_set').values_list('name','address','phone_number','gender','state','status__status','status__id','id')
    for x in stat:
        print(x)
    
    
    
    return render(request,'viewstatus.html',{'customers':stat})

def status(request):
    stat = Customer.objects.all
    
    return render(request,'status.html',{'customers':stat})

def editstatus(request, pk,customer):
    statusid = pk
    status = Status.objects.get(id=statusid)
    return render(request,'editstatus.html',{'id':statusid,'status':status,'customer':customer})

def updatestatus(request):
    if request.method == 'POST':
        id = request.POST['id']
        status = request.POST['status']
        Status.objects.filter(id=id).update(status=status)
        # b = Status.objects.get(id=id)
        # b.status = status
        # b.save()
        msg = "Hi, Status has been update to {status}"
        return redirect('viewstatus')
    
def deletecustomer(request,pk):
    Customer.objects.filter(id=pk).delete()
    
    return redirect('editcustomers')

def customerinfo(request):
    customer = Customer.objects.all
    
    return render(request,'customerinfo.html',{'customer':customer})

def editall(request,pk,name,address,phone_number,gender,state,loan_offer):
    customerid = pk
    name = Customer.objects.get(id=customerid)
    
    
    return render(request,'editall.html',{'id':customerid,'name':name,'address':address,'phone_number':phone_number,'gender':gender,'state':state,'loan_offer':loan_offer})

def updateall(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        state = request.POST['state']
        loan_offer = request.POST['loan_offer']
        Customer.objects.filter(id=id).update(name=name,address=address,phone_number=phone_number,gender=gender,state=state,loan_offer=loan_offer)
        # Customer.objects.filter(id=id).update(address=address)
        # Customer.objects.filter(id=id).update(phone_number=phone_number)
        # Customer.objects.filter(id=id).update(gender=gender)
        # Customer.objects.filter(id=id).update(state=state)
       
        return redirect('editcustomers')
    
def interest(request):
    rate = Customer.objects.prefetch_related('status_set').values_list('name','address','phone_number','gender','state','status__status','status__id','id','loan_offer')
    for r in rate:
        per20 = 0.2 * float(r[8])
        per30 = 0.3 * float(r[8])
        per50 = 0.5 * float(r[8])
        
    return render(request,'interest.html',{'rate':rate,'per20':per20,'per30':per30,'per50':per50})

def applyloan(request):
    customer = Customer.objects.all()
    return render(request,'applyloan.html',{'customers':customer})


