from django.shortcuts import render
from leads.models import Lead,product ,quotation
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  
import datetime
import os
from io import BytesIO
from crm import settings
from django.views.generic import View
from leads.forms import pdf_form

class GeneratePdf(View):
    def get(self, request, pk,):
        try:
            leads = Lead.objects.filter(id = pk)
        except:
            return HttpResponse("505 Not Found")
        date = datetime.datetime.today().date()
        quotations = quotation.objects.filter(lead_id = pk).last()
        context = {
            'leads': leads,
            "quotations" : quotations,
            "date" : date,
        }
        pdf = render_to_pdf('leads/pdf_report.html', context)
        for a in leads:
            b= a.first_name
            c = a.last_name
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"{b} {c} {datetime.datetime.now()}" + ".pdf"
            # content = "attachment; filename=%s" %(filename)    #for direct download
            content = "inline; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
#for adding image to pdf in future use
def fetch_resources(uri, rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path 

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def helper(request,pk):
    lead = Lead.objects.get(id=pk)
    leads = Lead.objects.filter(id = pk)
    form = pdf_form()
    if request.method =="POST":
        form = pdf_form(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        "form":form,
        "lead":lead
    }
    return render(request, "leads/helpers.html", context)


# def pdf_create(pk):
#    leads = Lead.objects.all()
#    products = product.objects.all()
#    date = datetime.datetime.today().date()
#    #leads = Lead.objects.filter(id=pk)
#    template_path = 'leads/pdf_report.html'
#    context = {
#       'leads': leads,
#       'date' : date
#    }
#    response = HttpResponse(content_type='application/pdf')
#    #response['Content-Disposition'] = 'attachment; filename="Quoation.pdf"' for direct download
#    response['Content-Disposition'] = ' filename="Quoation.pdf"'
#    template = get_template(template_path)
#    html = template.render(context)
#    pisa_status = pisa.CreatePDF(
#       html, dest=response)
#    if pisa_status.err:
#       return HttpResponse('We had some errors <pre>' + html + '</pre>')
#    return response
