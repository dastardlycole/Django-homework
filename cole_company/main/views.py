from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about_us(request):
    return render(request,'about.html')

def contact_us(request):    
    return render(request,'contact.html')