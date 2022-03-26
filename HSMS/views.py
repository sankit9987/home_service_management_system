from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer,User
# Create your views here.
def user_login(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user:
            login(request, user)
            messages.success(request,"Login Successfully!!!") 
            return redirect("index")
        else:
             messages.error(request,"Please check username and password!!!")
    return render(request,"login.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})
def user_logout(request):
    logout(request)
    return redirect("index")
def index(request):
    category=service_category.objects.all()
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"index.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services,"category":category})

def about_us(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"about-us.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def change_location(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"change-location.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def contact_us(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"contact-us.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def faq(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"faq.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def privacy(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"privacy.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def register(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']
        password_confirmation = request.POST['password_confirmation']
        image = request.FILES['image']
        if password==password_confirmation:
            user = User.objects.create_user(email=email,password=password)
            user.is_customer=True
            user.save()
            Customer.objects.create(user=user,name=name,address=address,mobile_no=phone,image=image)
            return redirect('user_login')
        else:
            messages.error(request,"Password Didn't match ")
    return render(request,"register.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def service_categories(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"service-categories.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def service_details(request,id):
    if request.method=='POST':
        serv = request.POST['serv']
        msg = request.POST['msg']
        cust = Customer.objects.get(user=request.user)
        serv = service.objects,get(id=id)
        Feedback.objects.create(serv=serv,customer=cust,msg=msg)
        return redirect("service_details/id")
   
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    s=service.objects.filter(service_sub_category=id)
    return render(request,"service-details.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services,'s':s})

def service_by_category(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"services-by-category.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def terms_of_use(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    return render(request,"terms-of-use.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

def product(request,id):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)

    s = service.objects.filter(service_sub_category=id)
    return render(request,"product.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services,"s":s})
    
def change_password(request):
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    if request.method=='POST':
        current_password = request.POST['cupassword']
        new_password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if new_password==confirm_password:
            user = User.objects.get(id=request.user.id)
            p = user.check_password(current_password)
            if p==True:
                user.set_password(new_password)
                user = authenticate(email=user.email,password=new_password)
                if user:
                    login(request,user)
                    messages.success(request,"Password Change !!!") 
                    return redirect("change_password")
            else:
                messages.error(request, "Current Password didn't match")
        else:
            messages.error(request, "Password didn't match")
    return render(request, "change-password.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

        
def edit(request):
    if request.method=='POST':
        name = request.POST['name']
        address = request.POST['address']
        mobile = request.POST['mobile']
        Customer.objects.filter(user=request.user.id).update(name=name,address=address,mobile_no=mobile)
        messages.success(request, "Update Successfully!!!")
        return redirect("edit")
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    print(request.user.id)
    user = Customer.objects.filter(user=request.user.id)
    print(user)
    return render(request, "edit-profile.html",{"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services,"user":user}) 

def booking(request):
    if request.method=='POST':
        user = request.user
        ser = request.POST['service']
        amount = request.POST['amount']
        s = request.POST['service_pro']
        stat = "Pending"
        se = service.objects.filter(id=ser)
        cus = Customer.objects.get(user=request.user)
        ser = Service_provider.objects.get(name=s)
        Booking.objects.create(customer=cus,service_provider=ser,ser=se[0],amount=amount,status=stat)
        return redirect("my_booking")

def order(request):
    return render(request, "order.html")

def my_booking(request):
    cust = Customer.objects.get(user=request.user)
    s = Booking.objects.filter(customer=cust)
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)

    return render(request, "my-booking.html",{'s':s,"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})



def search(request):
    
    ac=subcategory.objects.filter(category=2)
    home_need=subcategory.objects.filter(category=3)
    appliances=subcategory.objects.filter(category=4)
    home_cleaning=subcategory.objects.filter(category=5)
    special_services=subcategory.objects.filter(category=6)
    q = request.GET['q']
    s = service.objects.filter(title__icontains=q)
    return render(request, "search.html",{'s':s,'q':q,"Ac":ac,"home_need":home_need,"appliances":appliances,"home_cleaning":home_cleaning,"special_services":special_services})

