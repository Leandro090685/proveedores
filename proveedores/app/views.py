from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Proveedor



def index(request):
    return render (request,"index.html")

def new_prov(request):
    if request.method == "POST":
        form = forms.FormularioProveedor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app:newprov"))
    else:
        form = forms.FormularioProveedor
    ctx = {"form":form}
    return render (request,"createprov.html",ctx)

def view_prov(request):
    prov = Proveedor.objects.all()
    ctx = {"prov":prov}
    return render (request,"viewprov.html",ctx)

def delete_prov(request, id):
    prov = Proveedor.objects.get(id=id)
    prov.delete()
    return HttpResponseRedirect(reverse("viewprov"))

