from django.shortcuts import render

# Create your views here.

def salestype(request):
    return render(request, 'salestype.html'
                    , {})