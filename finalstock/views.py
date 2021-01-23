from django.shortcuts import render
from deviceqc.models import yes_deviceqc, no_deviceqc
from django.http import HttpResponseRedirect
from xlsxwriter.workbook import Workbook as book
from xlsxwriter.worksheet import Worksheet as sheet
import io

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# Create your views here.

def finalstock_view(request):

    yes_deviceqc_items = yes_deviceqc.objects.all()
    total_yes = yes_deviceqc_items.count()

    no_deviceqc_items = no_deviceqc.objects.all()
    total_no = no_deviceqc_items.count()

    args={

        'yes_deviceqc_items': yes_deviceqc_items,
        'total_yes': total_yes,
        'no_deviceqc_items': no_deviceqc_items,
        'total_no': total_no

    }

    return render(request, 'finalstock.html', args)

def finalactions(request):
    if 'download' in request.POST:

        def get_yes_data():
            yes_values = yes_deviceqc.objects.all().values()
            return yes_values

        def get_no_data():
            no_values = no_deviceqc.objects.all().values()
            return no_values

        output = io.BytesIO()

        yes_count = yes_deviceqc.objects.all().count()
        no_count = no_deviceqc.objects.all().count()


    if 'back' in request.POST:
        return HttpResponseRedirect('/cognitive/deviceqc')
