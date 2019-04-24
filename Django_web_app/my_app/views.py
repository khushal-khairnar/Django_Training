from django.shortcuts import render
from .models import Customer
import datetime
# Create your views here.
from django.http import HttpResponse
from django.template import loader

from my_app.forms import CustomerForm
from my_app.forms import Company_Form

def index(request):
    #template=loader.get_template()
    #name={
     #   'student':'Ganesh'
     #}
    # customer_obj = Customer.objects.get(id=2)
    #cust=CustomerForm()
    comp=Company_Form()
    return render(request,'index.html',{'form':comp})