from django.shortcuts import render
from .models import createitems
from django.http import HttpResponseRedirect
# Create your views here.

def create_view(request):
    return render(request, 'create.html', {})

def create_new(request):
    prod_name = request.POST['prod_name']
    description = request.POST['description']
    cprod_id = request.POST['cprod_id']
    vendor = request.POST['vendor']
    invoice_number = request.POST.get('invoice_number', True)
    quantity = request.POST['quantity']

    new_create_item = createitems(prod_name, description, cprod_id, vendor,
                                  invoice_number, quantity)
    new_create_item.save()

    args = {
        'cprod_id':cprod_id,
        'description':description,
        'vendor':vendor,
        'invoice_number':invoice_number,
        'quantity':quantity
    }
    return HttpResponseRedirect('/cognitive/device', args)