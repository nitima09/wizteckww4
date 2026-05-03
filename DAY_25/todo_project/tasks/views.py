from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from tasks.forms import *

# Create your views here.
def Register_page(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if password==confirmpassword:
            CustomInfoModel.objects.create_user(
            fullname=fullname,
            username=username,
            email=email,
            password=password
            )
            return redirect('login-page')
    return render (request, 'register.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username , password=password)
    
        if user:
            login(request, user)
            return redirect('home_page')
        else:
            print("Invalid Credential")
    
    return render(request, 'login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('login-page')

@login_required
def home_page(request):
    
    return render(request, 'home_page.html')



def profile_page(request):
    return render(request,'profile.html')


def profile_update(request):
    try:
        user_data = request.user.user_profile
    except ProfileModel.DoesNotExist:
        user_data = None
    
    if request.method == 'POST':
        form_data = UpdateProfileForm(
            request.POST,
            request.FILES,
            instance = user_data
        )
    
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('profile_page')
        
    form_data = UpdateProfileForm(instance=user_data)
    
    context = {
        'form_data':form_data,
        'title':'Update profile info',
        'btn_name':'Update'
    }
    return render(request,'master/base-form.html',context)

def product_list(request):
    product_data = ProductModel.objects.all()
    context={
        'product_data':'product_data'
    }
    
    return render(request,'prodect-list.html',context)


def add_product(request):
    if request.method =='POST':
        form_data = ProductForm(request.POST)
        if form_data.is_valid():
            form_data = form_data.save(commit=False)
            form_data.created_by = request.user
            form_data.total_amount = form_data.price * form_data.qty
            form_data.save()
            return redirect('product_list')
    form_data = ProductForm()
    context = {
        'form_data':form_data,
        'form_title':'Add product Info',
        'form_btn':'Add Product',
    }        
            
    return render(request,'master/base-form.html',context)