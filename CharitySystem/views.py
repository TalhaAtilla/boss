from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
import stripe
# Create your views here.
stripe.api_key = 'sk_test_TjwJ8KIE4pM0zUDkkubD4kvV00PipgfR59'

def about(request):
    return render(request, 'CharitySystem\self.html')
    
def home(request):
    return render(request, 'CharitySystem\home.html')    

def calibrate(request):
    return render(request, 'CharitySystem\calibrate.html')    

def cal1(request):
    return render(request, 'CharitySystem\cal1.html')    

def cal2(request):
    return render(request, 'CharitySystem\cal2.html')    

def software(request):
    return render(request, 'CharitySystem\software.html')    

def sof1(request):
    return render(request, 'CharitySystem\sof1.html')    

def sof2(request):
    return render(request, 'CharitySystem\sof2.html')    

def products(request):
    return render(request, 'CharitySystem\products.html')

def pro1(request):
    return render(request,"CharitySystem\pro1.html")

def pro2(request):
    return render(request,"CharitySystem\pro2.html")    

def pro3(request):
    return render(request,"CharitySystem\pro3.html")

def pro4(request):
    return render(request,"CharitySystem\pro4.html")    

def Atex(request):
    return render(request,"CharitySystem\Atex.html")    

def Ax1(request):
    return render(request,"CharitySystem\Ax1.html")    

def Ax2(request):
    return render(request,"CharitySystem\Ax2.html")    