from django.urls import path
from .import views

app_name = "app"

urlpatterns = [
    path("",views.index,name="index"),
    path("createprov/", views.new_prov, name="newprov"),
    path("viewprov/", views.view_prov, name="viewprov"), 
    path("deleteprov/<id>", views.delete_prov, name="deleteprov"),
    
    ]