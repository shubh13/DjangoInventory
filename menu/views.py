from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def menuview(request):

    args = {}

    return render(request, 'menu.html', args)

def menu_response(request):
    if 'create' in request.POST:
        return HttpResponseRedirect('/cognitive/create')

    if 'device' in request.POST:
        return HttpResponseRedirect('/cognitive/device')

    if 'devicetest' in request.POST:
        return HttpResponseRedirect('/cognitive/deviceqc')

    if 'bill' in request.POST:
        return HttpResponseRedirect('/cognitive/salestype')

    if 'initial_stock' in request.POST:
        return HttpResponseRedirect('/cognitive/view')

    if 'final_stock' in request.POST:
        return HttpResponseRedirect('/cognitive/finalstock')
