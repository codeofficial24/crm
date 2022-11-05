from django.contrib import messages
from .models import Ticket
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse 
# Create your views here.
from urllib.parse import _NetlocResultMixinStr
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
# from leads.models import Agent
from .forms import AgentModelForm , agentupdateform,userForm
from .models import agent
from django.contrib.auth.decorators import login_required
from leads.models import Lead , lead_activity
import datetime
from leads.decorators import unauthenticated_user, allowed_users, admin_only
from datetime import timedelta
# Create your views here.
@login_required(login_url='login')
def agent_list(request):
    agents = agent.objects.all()
    context = {
        "agents" : agents
    }
    return render(request,"agents/agent_list.html", context)
    # def get_queryset(self):
    #     organisation = self.request.user.userprofile
    #     return Agent.objects.filter(organisation=organisation)
@login_required(login_url='login')
def AgentCreateView(request):
    form =  AgentModelForm()
    if request.method == "POST":
        form = AgentModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("agents:agent-list")
    context = {
        "form": form
    }
    return render(request, "agents/agent_create.html", context)


@login_required(login_url='login')
def agentdetail(request,pk):
    agents = agent.objects.get(user_id=pk)
    form = agentupdateform(instance=agents)
    if request.method =="POST":
        form = agentupdateform(request.POST, instance=agents)
        if form.is_valid():
            form.save()
            return redirect("agents:agent-list")
    context = {
        "form":form,
        "agents" : agents
    }
    return render(request, "agents/agent_detail.html", context)



@login_required(login_url='login')
def dashboard(request):
    leads = Lead.objects.all()
    t_date=datetime.date.today()
    date_entry = ()
    query = request.GET.get('search')
    try:
        date_entry = query
        year, month, day = map(int, date_entry.split('-'))
        date = datetime.date(year, month, day)
    except:
        date=datetime.date.today()


    if request.method == 'GET':
        a = request.GET.get("stats")
        if a == "daily" :
            total = Lead.objects.filter(date_created__gte=datetime.datetime.now()-timedelta(days=1)).count()
        elif a == "week" :
            total = Lead.objects.filter(date_created__gte=datetime.datetime.now()-timedelta(days=7)).count()
        elif a == "month" :
            total = Lead.objects.filter(date_created__gte=datetime.datetime.now()-timedelta(days=30)).count()
        elif a == "year" :
            total = Lead.objects.filter(date_created__gte=datetime.datetime.now()-timedelta(days=365)).count()
        else:
            total = leads.count()
    activity = lead_activity.objects.select_related('lead_id').filter(scheduled_date = date)
    today_activity = lead_activity.objects.select_related('lead_id').filter(scheduled_date = t_date)
    activitytotal = today_activity.count()
    context = {
        "leads" : leads,
        "total" : total ,
        "date" : date,
        "activity" : activity ,
        "activitytotal" : activitytotal,
        't_date' : t_date
    }
    return render(request,"dashboard.html", context)



def agentdashboard(request):
    date_entry = ()
    query = request.GET.get('search')
    try:
        date_entry = query
        year, month, day = map(int, date_entry.split('-'))
        date = datetime.date(year, month, day)
    except:
        date=datetime.date.today()
    t_date=datetime.date.today()
    agents = request.user.id
    leads = Lead.objects.filter(agent = agents)
    activity_list = []
    activity_today = []
    for lead_id in leads:
        for lead_activity_obj in lead_activity.objects.filter(lead_id=lead_id,scheduled_date=date):
            activity_list.append(lead_activity_obj)
        for lead_activity_obj in lead_activity.objects.filter(lead_id=lead_id,scheduled_date=t_date):
           activity_today.append(lead_activity_obj)
    if request.method == 'GET':
        a = request.GET.get("stats")
        if a == "daily" :
            total = Lead.objects.filter(agent = agents,date_created__gte=datetime.datetime.now()-timedelta(days=1)).count()
        elif a == "week" :
            total = Lead.objects.filter(agent = agents,date_created__gte=datetime.datetime.now()-timedelta(days=7)).count()
        elif a == "month" :
            total = Lead.objects.filter(agent = agents,date_created__gte=datetime.datetime.now()-timedelta(days=30)).count()
        elif a == "year" :
            total = Lead.objects.filter(agent = agents,date_created__gte=datetime.datetime.now()-timedelta(days=365)).count()
        else:
            total = leads.count()
    activitytotal = len(activity_today)

    context = {
        "leads": leads,
        "total" : total ,
        "date" : date ,
        "activity" : activity_list ,
        "activitytotal" : activitytotal,
        't_date' : t_date
    }
    return render(request, "agentdashboard.html", context)



# class AgentUpdateView(LoginRequiredMixin, generic.TemplateView):
#     template_name = "agents/agent_update.html"
#     form_class = AgentModelForm

#     def get_success_url(self):
#         return reverse("agents:agent-list")



def index(request):
 tickets = Ticket.objects.order_by('-created_at')[:50]
 return render(request,'index.html', {'tickets': tickets})

def ticket_by_id(request, ticket_id):
 ticket = Ticket.objects.get(pk=ticket_id)
 return render(request, 'ticket_by_id.html', {'ticket':ticket})



def add_Ticket(request):
      form = userForm()
      if request.method == 'POST':
            form = userForm(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request,'Ticket Generated Successfully')
            else:  # display empty form
               form = userForm()  
      return render(request,'getdata.html',{'data': form}) 


def update_Ticket(request,ticket_id):  
   form = userForm()
   ticket = Ticket.objects.get(pk=ticket_id)
   form = userForm(request.POST or None, instance=ticket)
   if request.method == 'POST':
    if form.is_valid():
               form.save()  
               messages.success(request,'Ticket updated Successfully')
   return render(request,'update.html',{'data':form}) 

def delete_Ticket(request,ticket_id):
         ticket = Ticket.objects.get(pk=ticket_id)
         ticket.delete()
         messages.success(request,'Ticket deleted Successfully')
         return redirect('index')
         