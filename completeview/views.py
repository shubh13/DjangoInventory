from django.shortcuts import render
from device.models import device
from django.http import HttpResponseRedirect, HttpResponse
import xlsxwriter
from xlsxwriter.workbook import Workbook as book
from xlsxwriter.worksheet import Worksheet as sheet
import io

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# Create your views here.

def completeview_view(request):

    display_items = device.objects.all()
    total = display_items.count()

    args = {

        'display_items': display_items,
        'total': total

    }

    return render(request, 'completeview.html',args)

def viewpage(request):

    if 'back' in request.POST:

        return HttpResponseRedirect('/cognitive/device')

    if 'download' in request.POST:

        def get_device_data():
            device_data = device.objects.all().values()
            return device_data

        count = device.objects.all().count()

        output = io.BytesIO()

        book = xlsxwriter.Workbook(output, {'tmpdir':'/home/shubhadeep/cognitive/'})
        sheet = book.add_worksheet('Device Data')

        cell_format = book.add_format({'bold':True, 'bg_color':'yellow'})
        date_format = book.add_format({'num_format':'dd/mm/yyyy'})
        text_format = book.add_format({'align':'center'})

        sheet.write('A1', 'Product Id', cell_format)
        sheet.write('B1', 'Device Sl. No.', cell_format)
        sheet.write('C1', 'Device Id', cell_format)
        sheet.write('D1', 'Device Barcode', cell_format)
        sheet.write('E1', 'Device DOP', cell_format)
        sheet.write('F1', 'Device HSN', cell_format)

        col_num=0
        row_num=0

        for i in range(count):
            data=get_device_data()
            for row_num, cell_data in enumerate(data):
                sheet.set_column(row_num, col_num, 15)
                sheet.write_row(row_num+1, col_num, cell_data.values(), text_format)

        book.close()

        output.seek(0)

        filename = 'Inventory_Data.xlsx'

        response = HttpResponse(output,
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response

    if 'delete' in request.POST:
        device.objects.filter(device_id=request.POST.get('item')).delete()
        return HttpResponseRedirect('/cognitive/view')
