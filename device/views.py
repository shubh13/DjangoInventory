from django.shortcuts import render
from .models import device as dv
from create.models import createitems
from django.http import HttpResponseRedirect as hrr
from django.contrib import messages

# Create your views here.

def device(request):

    new_create = createitems.objects.all()
    total_items = createitems.objects.all().count()

    args={'new_create':new_create[total_items-1]}

    return render(request, 'device.html', args)

def add_device(request):

    new_device_item = dv(
        prod_id=request.POST['prod_id'],
        device_sl=request.POST.get('device_sl', False),
        device_id=request.POST['device_id'],
        device_bcode=request.POST['device_bcode'],
        device_date=request.POST.get('device_purchase', False),
        device_hsn=request.POST['device_hsn'])

    flag = False

    if 'add' in request.POST:

        check_items = dv.objects.all()
        total = check_items.count()

        flag=True

        prod_id = request.POST['prod_id']
        check_sl = request.POST['device_sl']
        check_id = request.POST['device_id']

        if check_sl=='':
            messages.error(request, 'Serial Number cannot be empty')
            return hrr('/cognitive/device')
        elif check_id=='':
            messages.error(request, 'Device id cannot be empty')
            return hrr('/cognitive/device')
        else:
            pass

        for i in range(total):
            if check_id==check_items[i].device_id:
                flag=False

        if flag:
            messages.success(request, 'Data Saved Successfully')
            new_device_item.save()
            return hrr('/cognitive/device')
        else:
            messages.error(request, 'Data already exists')
            return hrr('/cognitive/device')

    if 'view' in request.POST:
        return hrr("/cognitive/view")

    if 'proceed' in request.POST:
        return hrr('/cognitive/deviceqc')
