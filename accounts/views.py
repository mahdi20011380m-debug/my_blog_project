from django.shortcuts import render , redirect 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as auth_login 
# Create your views here. 
 
 
 
def register_view(request): 
    if request.method == "POST": 
        username = request.POST.get("username") 
        password = request.POST.get("password") 
 
        if User.objects.filter(username=username).exists(): 
            return render(request, "accounts/register.html", {"error": "این نام کاربری قبلاً ثبت شده است"}) 
 
        user = User.objects.create_user(username=username, password=password) 
        user.save() 
         
 
 
        auth_login(request, user) 
 
        return redirect("landing")   
 
    return render(request, "accounts/register.html")  
 
 
 
def login_view(request): 
    if request.method == "POST": 
        username = request.POST.get("username") 
        password = request.POST.get("password") 
 
        user = authenticate(request, username=username, password=password) 
        if user: 
            auth_login(request, user) 
            return redirect("index")    
  
        return render(request, "accounts/login.html", {"error": "یوزرنیم یا پسورد اشتباه است"}) 
 
    return render(request, "accounts/login.html") 
 
 
 
 