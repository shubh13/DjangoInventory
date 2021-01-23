from django.shortcuts import render

# Create your views here.

def invoiceview(request):
    return render(request, "invoice.html", {})
