from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Futsal


def home(request):
    return render(request, template_name='myapp/home.html')

def outdoor(request):
    return render(request, template_name='myapp/outdoor.html')

def indoor(request):
    return render(request, template_name='myapp/indoor.html')

def contact(request):
    return render(request, template_name='myapp/contact.html')

def futsal(request):
    futsal = Futsal.objects.all()
    return render(request, template_name='myapp/futsal.html', context={"futsal": futsal})

def basketball(request):
    return render(request, template_name='myapp/basketball.html')

def cricket(request):
    return render(request, template_name='myapp/cricket.html')

def detail_futsal(request, id):
    futsal = Futsal.objects.get(id=id)
    return render(request,template_name="forms/detail_futsal.html", context={"futsal": futsal})


def add_futsal(request):
    if request.method.lower() == "post":
         futsal_name = request.POST.get("futsalname")
         Futsal.objects.create(name=futsal_name)
         return redirect("add_classroom")
    futsals = Futsal.objects.all()

    return render (request, template_name="myapp/add_futsal.html", context={"futsals": futsals})
    






