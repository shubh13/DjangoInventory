from django.shortcuts import render
from create.models import createitems
from .models import yes_deviceqc, no_deviceqc
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def deviceqc_view(request):

    toggle_ids = createitems.objects.all()

    args={
        'toggle_ids':toggle_ids
    }
    
    return render(request, 'deviceqc.html', args)

def test_device(request):

    if 'submit_test' in request.POST:

        prod_id = request.POST['prod_id']
        device_id = request.POST['device_id']
        device_bcode = request.POST['device_bcode']
        qc_passed = request.POST['option']

        if qc_passed=='Yes':
            if device_id=='':
                messages.error(request, 'Device Id cannot be empty')
                return HttpResponseRedirect('/cognitive/deviceqc')
            else:
                yes_deviceqc(prod_id, device_id, device_bcode, qc_passed).save()
                messages.success(request, 'Device Passed QC \n Data Saved')
                return HttpResponseRedirect('/cognitive/deviceqc')

        else:
            if device_id=='':
                messages.error(request, 'Device Id cannot be empty')
                return HttpResponseRedirect('/cognitive/deviceqc')
            else:
                no_deviceqc(prod_id, device_id, device_bcode, qc_passed).save()
                messages.success(request, 'Device Failed QC \n Data Saved')
                return HttpResponseRedirect('/cognitive/deviceqc')

    if 'view_final' in request.POST:
        return HttpResponseRedirect('/cognitive/finalstock')

    if 'proceed' in request.POST:
        return HttpResponseRedirect('/cognitive/salestype')
