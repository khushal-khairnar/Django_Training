from django import forms


from emp_app.models import (User,
                    University,
                    Academic,
                    Company,
                    Experience
                             )

class Registraion_Form(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"


class University_form(forms.ModelForm):
    class Meta:
        model=University
        fields="__all__"

class Academic_form(forms.ModelForm):
    class Meta:
        model=Academic
        fields="__all__"
class Company_form(forms.ModelForm):
    class Meta:
        model=Company
        fields="__all__"
class Experience_form(forms.ModelForm):
    class Meta:
        model=Experience
        fields="__all__"
