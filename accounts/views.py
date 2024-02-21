from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


# base page - nav bar
def index(request):
    return render(request, 'index.html')

# page for customer registration
def customerReg(request):
    form = customerForm()
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form = form.save()
    return render(request, 'accounts/customer.html', {'form':form})

# page for vender registration
def venderReg(request):
    form = vendorForm()
    return render(request, 'accounts/vender.html', {'form':form})

