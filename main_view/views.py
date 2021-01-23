from django.shortcuts import render
from django.contrib import messages
from .models import user_signup
from django.http import HttpResponseRedirect
from register.models import registeritems as ri

def main_view(request):
    return render(request, 'main_view.html', {})

def new_login(request):

    if 'register' in request.POST:
        return HttpResponseRedirect('/cognitive/register')

    if 'login' in request.POST:

        flag = False

        username = request.POST['sign_username']
        password = request.POST['sign_password']

        if username=='':
            messages.error(request, 'Enter the username')
            return HttpResponseRedirect('/cognitive')
        elif password=='':
            messages.error(request, 'Please enter the password')
            return HttpResponseRedirect('/cognitive')
        else:
            pass

        r_data = ri.objects.all()
        total_data = ri.objects.all().count()

        for i in range(total_data):
            if username==r_data[i].emp_id and password==r_data[i].password:
                flag = True

        if flag:
            messages.success(request, "Welcome to Cognitive ERP")
            return HttpResponseRedirect('/cognitive/menu')
        else:
            messages.error(request, "Wrong username or password")
            return HttpResponseRedirect('/cognitive')
