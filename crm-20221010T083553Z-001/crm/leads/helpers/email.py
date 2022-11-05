from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  
import datetime
from leads.models import  product , Lead
import os
from io import BytesIO
from crm import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage

def send_my_mail(request, pk):
    leads = Lead.objects.filter(id = pk).only('email')
    for a in leads:
        b= a.email
    template = get_template('leads/pdf_report.html')
    leads = Lead.objects.filter(id = pk)
    products = product.objects.all()   
    date = datetime.datetime.today().date()
    data = {
        'leads': leads,
        "products" : products,
        "date" : date
    }
    html  = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = 'Quoation.pdf'
    # mail_subject = 'Requsted Quoation Details'
    template = get_template('leads/sendemail.html')
    to_email = b
    # print(to_email) 
    email = EmailMultiAlternatives(
        'Requsted Quoation Details',
        'Hi,This is in regards to your quoation request.We have attached a pdf with this mail.Thanks for trusting us and using our services!Sincerely,BuyByeQ Team',
        'unknownhuman196@gmail.com',
        [to_email],
        )
        
    email.attach(filename, pdf, 'application/pdf')
    email.send(fail_silently=False)
       
    return render(request, 'leads/sendemail.html')




    # send_mail(
    #     'This is the subject of my mail hello everybody',
    #     'This is the test message body from django product management website',
    #     'unknownhuman196@gmail.com',
    #     ['atipradmishra2003@gmail.com'],
    #     fail_silently=False
    # )


