from django.forms import ModelForm
from django import forms

from my_app.models import Customer
from my_app.models import Company

class CustomerForm(ModelForm):

    class Meta:
        model=Customer
        fields="__all__"

class Company_Form(forms.Form):
    c_name=forms.CharField(label="Enter company Name", max_length=12)
    c_add=forms.CharField(label="Enter company address",max_length=32)

