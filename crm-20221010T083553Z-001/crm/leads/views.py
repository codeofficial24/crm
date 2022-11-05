from django.core.mail import send_mail
from urllib.request import Request
from django.shortcuts import render, redirect, reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from .forms import  *
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from agents.models import agent
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from .resources import LeadResource
from tablib import Dataset
from leads.helpers import pdf


@receiver(post_save, sender=User)
def handle_new_job(sender, **kwargs):
    if kwargs.get('created', False):
        user = kwargs.get('instance')
        g = Group.objects.get(name='agent')
        user.groups.add(g)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('landing-page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'registration/signup.html', context)

@unauthenticated_user
def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('landing-page')
			else:
				messages.info(request, 'Username OR password is incorrect')

		return render(request, 'registration/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


# class SignupView(CreateView):
#     template_name = "registration/signup.html"
#     form_class = UserCreationForm

#     def get_success_url(self):
#         return reverse("login")

def LandingPageView(request):
    leads = Lead.objects.all()
    total = leads.count()
    date = datetime.date.today()
    context = {
        "leads" : leads,
        "total" : total ,
        "date" : date
    }
    #return HttpResponse("Hello World")
    return render(request,"landing.html", context)


@login_required(login_url='login')
def lead_list(request):
    if request.user.is_staff == True :
        leads = Lead.objects.all()
    else:
        agents = request.user.id
        leads = Lead.objects.select_related('agent').filter(agent = agents)
    if request.method == "POST":
        lead_resource = LeadResource()
        dataset = Dataset()
        new_leads = request.FILES['myfile']

        imported_data = dataset.load(new_leads.read(),format='xlsx')
        for data in imported_data:
            value = Lead(
                data[0],
        		data[1],
        		data[2],
        		data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12]
        		)
            value.save()
            return redirect("/leads")
    context ={
        'leads' : leads
    }
    return render(request, "leads/lead_list.html" , context)

@login_required(login_url='login')
def lead_detail(request, pk ):
    if request.user.is_staff == True :
        lead = Lead.objects.get(id=pk)
    else:
        agents = request.user.id
        lead = Lead.objects.get(id=pk,agent = agents)
    y = Lead.objects.filter(id=pk)
    for x in y:
        import datetime
        age = (datetime.datetime.now() - x.date_created.replace(tzinfo=None)).days
    Lead_communication = lead_communication.objects.select_related('lead_id').filter(lead_id= lead).order_by('Date_created')
    Lead_activity = lead_activity.objects.select_related('lead_id').filter(lead_id= lead)
    form = Lead_communication_form
    lead_activity_form = Lead_activity_form
    if request.method == "POST":
        form = Lead_communication_form(request.POST)
        lead_activity_form = Lead_activity_form(request.POST)
        if form.is_valid():
            form.save()
            
    if request.method == "POST":
        lead_activity_form = Lead_activity_form(request.POST)
        if lead_activity_form.is_valid():
            lead_activity_form.save()
            

 
    context = {
        "lead": lead,
        "Lead_communication" : Lead_communication ,
        "Lead_activity" : Lead_activity ,
        "form" : form ,
        "Lead_activity_form" : lead_activity_form ,
        "age": age,
    }
    return render(request, "leads/lead_detail.html", context)



@login_required(login_url='login')
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

@login_required(login_url='login')
def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method =="POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("leads:lead-detail" , lead.pk)
    
    context = {
        "form":form,
        "lead":lead
    }
    return render(request, "leads/lead_update.html", context)

@login_required(login_url='login')
@admin_only
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads/all")



# class LeadListView(LoginRequiredMixin,ListView):
#     template_name = "leads/lead_list.html"
#     queryset = Lead.objects.all()
#     context_object_name = "leads"

# class LeadDetailView(LoginRequiredMixin,DetailView):
#     template_name = "leads/lead_detail.html"
#     form_class = LeadModelForm
#     queryset = Lead.objects.all()
#     context_object_name = "lead"

#     def get_success_url(self):
#         return reverse("leads:lead-list")

#     def form_valid(self, form):
#         #TODO send email
#         send_mail(
#             subject="A lead has been created",
#             message="Go to the site to check the new lead",
#             from_email="test@test.com", recipient_list=["test2@test.com"]

# #         )
#         return super(LeadDetailView,self).form_valid(form)
    #queryset = Lead.objects.all()
    #
    

# class LeadCreateView(LoginRequiredMixin,CreateView):
#     template_name = "leads/lead_create.html"
#     form_class = LeadModelForm

#     def get_success_url(self):
#         return reverse("leads:lead-list")

#     def form_valid(self, form):
#         #TODO send email
#         send_mail(
#             subject="A lead has been created",
#             message="Go to the site to check the new lead",
#             from_email="test@test.com", recipient_list=["test2@test.com"]

#         )
#         return super(LeadCreateView,self).form_valid(form)


# class LeadUpdateView(LoginRequiredMixin,UpdateView):
#     template_name = "leads/lead_update.html"
#     queryset = Lead.objects.all()
#     form_class = LeadModelForm

#     def get_success_url(self):
#         return reverse("leads:lead-list")

# class LeadDeleteView(LoginRequiredMixin,DeleteView):
#     template_name = "leads/lead_delete.html"
#     form_class = LeadModelForm

#     def get_success_url(self):
#         return reverse("leads:lead-list")

# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads/all")
#     context = {
#         "form":form,
#         "lead":lead
#     }
#     return render(request, "leads/lead_update.html", context)
    
# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         print("Receiving a POST request")
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             print("The form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age=age,
#                 agent=agent
#             )

#             print("The lead has been created")
#             return redirect("/leads/all")

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


# @login_required(login_url='login')
# def agentPage(request):
#     agents = request.user.id
#     leads = Lead.objects.select_related('agent').filter(agent = agents)
#     if request.method == "POST":
#         lead_resource = LeadResource()
#         dataset = Dataset()
#         new_leads = request.FILES['myfile']

#         imported_data = dataset.load(new_leads.read(),format='xlsx')
#         for data in imported_data:
#             value = Lead(
#                 data[0],
#         		data[1],
#         		data[2],
#         		data[3],
#                 data[4],
#                 data[5],
#                 data[6],
#                 data[7],
#                 data[8],
#                 data[9],
#                 data[10],
#                 data[11],
#                 data[12]
#         		)
#             value.save()
#             return redirect("/leads")

#     context = {
#         "leads": leads,
#         "agents" : agents
#     }
#     return render(request, "leads/agent_lead.html", context)
