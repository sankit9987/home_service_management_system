from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

def dashboard(request):
    se = Service_provider.objects.get(user=request.user)
    s = service.objects.filter(user=se).count()
    b = Booking.objects.filter(service_provider=se).count()
    return render(request, "service/dashboard.html",{'se':se,'s':s,'b':b})

def add_service(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        price = request.POST['price']
        discount = request.POST['discount']
        Feature = request.POST['Feature']
        image = request.FILES['image']
        total = int(price)-int(discount)
        user = User.objects.get(id=request.user.id)
        quantity = 1
        category = service_category.objects.get(id=category)
        sub = subcategory.objects.get(id=sub_category)
        service.objects.create(title=title,description=description,price=price,total=total,discount=discount,feature=Feature,image=image,user=user,quantity=quantity,category=category,service_sub_category=sub)
        messages.success(request, "Add Successfully!!")
        return redirect("view_service")
    category = service_category.objects.all()
    sub = subcategory.objects.all()
    se = Service_provider.objects.get(user=request.user)
    return render(request, "service/add_service.html",{"category":category,"sub":sub,'se':se})

def view_service(request):
    se = Service_provider.objects.get(user=request.user)
    ser = service.objects.filter(user=se)
    
    return render(request, "service/view-service.html",{'ser':ser,'se':se})

def order(request):
    user = User.objects.get(id=request.user.id)
    se = Service_provider.objects.get(user=user)
    ser = Booking.objects.filter(service_provider=se.id)
    return render(request, "service/order.html",{'order':ser,'se':se})
   
def service_delete(request,id):
    ser = service.objects.get(id=id)
    ser.delete()
    messages.success(request, "Delete Successfully!!")
    return redirect("view_service") 

def service_view(request,id):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        discount = request.POST['discount']
        Feature = request.POST['Feature']
        total = int(price)-int(discount)
        service.objects.filter(id=id).update(title=title,description=description,price=price,total=total,discount=discount,feature=Feature)
        if request.FILES:
            image = request.FILES['image']
            ser = service.objects.get(id=id)
            os.remove(ser.image.path)
            ser.image = image
            ser.save()

        messages.success(request, "Update Successfully!!")
        return redirect("view_service")


    ser = service.objects.filter(id=id)
    se = Service_provider.objects.get(user=request.user)
    return render(request,"service/view-service-detail.html",{"ser":ser,'se':se}) 

def view_order(request,id):
    
    ser = Booking.objects.filter(id=id)
    se = Service_provider.objects.get(user=request.user)
    return render(request, "service/view_order.html",{'order':ser,'se':se})


def add_service_provider(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']
        password_confirmation = request.POST['password_confirmation']
        c = request.POST['category']
        if password==password_confirmation:
            user = User.objects.create_user(email=email,password=password)
            user.is_service=True
            user.save()
            c = service_category.objects.get(id=c)
            Service_provider.objects.create(user=user,name=name,address=address,mobile_no=phone,category=c)
            return redirect('user_login')
        else:
            messages.error(request,"Password Didn't match ")
    c = service_category.objects.all()
    return render(request, "add-service-provider.html",{'c':c})
