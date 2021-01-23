from django.shortcuts import render, redirect
from .models import registeritems
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):

    return render(request, 'register.html', {})

def add_register(request):

    new_data_item = registeritems(
        emp_id = request.POST['emp_id'],
        name = request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        password = request.POST['password']
    )

    new_data_item.save()

    return HttpResponseRedirect('/cognitive')
