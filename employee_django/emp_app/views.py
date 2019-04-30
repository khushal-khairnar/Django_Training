from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from emp_app.forms import ( Registraion_Form,
                    University_form,
                    Company_form,
                    Experience_form,
                    Academic_form
                            )
'''
def registraion(request):
    context= {}
    reg=Registraion_Form(request.POST)
    if reg.is_valid():
        reg.save()

    uni = University_form(request.POST)
    if uni.is_valid():
        uni.save()


    acd=Academic_form(request.POST)
    if acd.is_valid():
        acd.save()
    cmp=Company_form(request.POST)
    if cmp.is_valid():
        cmp.save()
    exp = Experience_form(request.POST)
    if exp.is_valid():
        exp.save()
    context={'form':reg,'form2':uni,'form3':acd,'form4':cmp,'form5':exp}

    return render(request,"index.html",context)
'''
def registraion(request):

    if request.method == "POST":
        reg = Registraion_Form()
        uni = University_form()
        acd = Academic_form()
        cmp = Company_form()
        exp = Experience_form()

        if reg.is_valid() and uni.is_valid() \
                and acd.is_valid() and cmp.is_valid() \
                                        and exp.is_valid():

                reg.save()
    else:
        reg = Registraion_Form()
        uni = University_form()
        acd = Academic_form()
        cmp = Company_form()
        exp = Experience_form()
    context = {'form': reg, 'form2': uni, 'form3': acd, 'form4': cmp, 'form5': exp}
    return render(request, "index.html", context)


        #reg=Registraion_Form()

    # context={'form':reg}
        #uni = University_form()
    #acd = Academic_form()
    #cmp = Company_form(request.POST)
    #exp = Experience_form()
    #context = {'form': reg, 'form2': uni, 'form3': acd, 'form4': cmp, 'form5': exp}

