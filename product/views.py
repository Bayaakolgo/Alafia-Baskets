from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Product
from django.shortcuts import get_object_or_404
import os
from django.contrib.auth.decorators import login_required

# Create your views here.
# DEFAULT VIEWS
def about(request):
    return render(request, 'product/about.html')

def home(request):
    return render(request, 'product/home.html')

# ADMIN VIEWS
def adminlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('admin-dashboard') #Admin dashboard for admin only.
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request=request, template_name='product/admin_login.html', context={'login_form':form})

@login_required
def admin_dashboard(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'product/admin_dashboard.html', context=context)

@login_required
def admin_add_product(request):
    if request.method == 'POST':
        product = Product()
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')

        if len(request.FILES) != 0:
            product.image = request.FILES['image']
        
        product.save()
        messages.success(request, "Product Added Successfully")
        return redirect('admin-dashboard') #Admin dashboard
    return render(request, 'product/admin_add_product.html')

@login_required
def admin_update_product(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(product.image) > 0:
                os.remove(product.image.path)
            product.image = request.FILES['image']
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('admin-dashboard')
    context = {'product':product}
    return render(request, 'product/admin_update_product.html', context)

@login_required
def admin_delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('admin-dashboard')

def admin_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

# USER VIEWS
def product_catalogue(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'product/product_catalogue.html', context)
