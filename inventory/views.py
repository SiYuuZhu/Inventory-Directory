from django.shortcuts import render,get_object_or_404
from inventory.models import Inventory
from django.http import HttpResponse

def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'AnInventory' : inventory
    }
    return render(request, 'inventory_detail.html', context)

