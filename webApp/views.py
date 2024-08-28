from django.shortcuts import render, redirect
from .forms import ApplicantForm,MyForm
from .models import Applicant
from django.http import HttpResponse

# Create your views here.
def lists(request):
    data = Applicant.objects.all()
    return render(request,'lists.html',{'data':data})

def apps(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            aage = form.cleaned_data['age']
            appls = Applicant.objects.create(first_name=f_name, last_name=l_name, age=aage)
            appls.save()
            return redirect('lists')
    form = ApplicantForm()
    return render(request,'apps.html',{'form':form})

def delete(request,id):
    dat = Applicant.objects.get(id=id)
    dat.delete()
    return redirect('lists')

def update(request,id):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            aage = form.cleaned_data['age']
            appls = Applicant.objects.create(first_name=f_name, last_name=l_name, age=aage)
            appls.save()
            return redirect('lists')
    applicant = Applicant.objects.get(pk=id)
    MyForm = ApplicantForm(initial={'first_name': applicant.first_name, 'last_name': applicant.last_name,'age': applicant.age})
    return render(request,'update.html',{'form':MyForm,'applicant':applicant})


def uprec(request,id):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            aage = form.cleaned_data['age']
            dat = Applicant.objects.get(id=id)
            dat.first_name = f_name
            dat.last_name = l_name
            dat.age = aage
            dat.save()
        return redirect('lists')
