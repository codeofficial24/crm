from dataclasses import field
from random import choices
from colorama import Style
from django.forms import ModelForm
from .models import Lead, lead_activity , lead_communication , Customer ,quotation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2' ]

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'agent',
            'size',
            'location',
            'phone_number',
            'designation',
            'email',
            'source',
            'stage',
            'status',
            'pincode',
        )
        widgets = {
            'email' : forms.EmailInput(attrs={'id' : 'email' , 'class':"box" , 'style':'left: 100px;top: 400px;', 'placeholder' : 'Emai**'}),
            'phone_number' : forms.NumberInput(attrs={'class':"box" , 'style':'left: 781px;top: 400px;', 'placeholder' : 'Phone Number**' , 'max_length': '10'}),
            'first_name' : forms.TextInput(attrs={'class':'box', 'style':'top: 220px; left: 101px;', 'placeholder' : 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':"box", 'style':'left: 781px; top: 220px;','placeholder' : 'Last Name'}),
            'agent' : forms.Select(choices=['test'],attrs={'class':'box', 'style':'top: 320px; left: 101px;', 'placeholder' : 'First Name'}),
            'size': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px;top: 670px;'}),
            'location': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px;top: 490px;'}),
            'designation': forms.TextInput(attrs={'class':"box" , 'style':'left: 781px;top: 670px;'}),
            'source': forms.TextInput(attrs={'class':"box" , 'style':'left: 100px;top: 580px;'}),
            'stage': forms.TextInput(attrs={'class':"box" , 'style':'left: 781px;top: 580px;'}),
            'status': forms.TextInput(attrs={'class':"box", 'style':'left: 781px;top: 310px;'}),
            'pincode': forms.TextInput(attrs={'class':"box", 'style':'left: 781px;top: 490px;'}),
        }


class Lead_communication_form(forms.ModelForm):
    class Meta:
        model = lead_communication 
        fields = (
            'lead_id',
            'message',
            'Type',
            'proablity',
            ) 

        widgets = {
            'lead_id' : forms.HiddenInput(attrs={'id' : 'lead_id',}),
            'message' : forms.Textarea(attrs={ 'id' : 'message', 'placeholder': 'Your Conversation here*', 'class' : 'box', 'cols': '50', 'rows': '5' }),
            'Type' : forms.HiddenInput(attrs={'id' : 'type', 'placeholder': 'Conversation Type','class' : 'box'}),
            'proablity' : forms.HiddenInput(attrs={ 'id' : 'proablity', 'placeholder': 'Proablity', 'class' : 'box'}),
        }



class Lead_activity_form(forms.ModelForm):
    class Meta:
        model = lead_activity
        fields = (
            'lead_id',
            'activity_name',
            'scheduled_date',
            'actual_date',
            'demo_status',
            )   
        widgets = {
            'lead_id' : forms.HiddenInput(attrs={'id' : 'activity_id'}),
            'scheduled_date' : forms.DateInput(attrs={'type' :"date"}),
            'activity_name' : forms.Select(choices=['ACTIVITY_CHOICES']),
            'actual_date' : forms.DateInput(attrs={'type' :"date"}),
            'demo_status' : forms.Select(choices=['STATUS_CHOICE']), 
        }
class customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'lead_id', 
            'org_name',
            'contact_name',
            'phone_number',
            'email', 
            'conversation_date',
            'renewal_date',
            'start_date',
            'subscription_used_date',
            'payment_cycle',
            'gst_no',
            )
        widgets = {
            'conversation_date' : forms.DateInput(attrs={'type' :"date"}),
            'renewal_date' : forms.DateInput(attrs={'type' :"date"}),
            'start_date' : forms.DateInput(attrs={'type' :"date"}),
            'subscription_used_date' : forms.DateInput(attrs={'type' :"date"}),
        }        




class pdf_form(forms.ModelForm):
    class Meta:
        model = quotation
        fields = (
            'lead_id',
            'quotation_file_name',
            'Quantity',
            'product_id',
            'price_offered',
            )   
        widgets = {
            'lead_id' : forms.HiddenInput(attrs={'id' : 'lead_id'}),
            'price_offered': forms.TextInput(attrs={'id':"p_id"}),
        }
