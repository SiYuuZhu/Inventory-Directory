from django.http import HttpResponse
from django.shortcuts import render
from inventory.models import Inventory

def home(request):
    inventorys = Inventory.objects.all()
    # print(inventorys)
    context = {
        'inventorys' : inventorys,
    }
    return render(request, 'home.html', context)