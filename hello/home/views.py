from django.shortcuts import render,HttpResponse

from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # so basically render takes 3 things 
    # 1 index
    # 2 template means index.html
    # 3 dictionary which is = context 
    context= {
        'variable1':'harshada',
        'variable2':'mango'

    }
    return render(request,'index.html',context)
    # return HttpResponse("Home page")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()

        # it is used to flash the success msg on page
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 