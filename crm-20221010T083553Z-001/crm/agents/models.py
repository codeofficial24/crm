from turtle import title
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User , Group


class agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    agent_name = models.CharField(max_length = 20)
    organisation = models.CharField(max_length = 30 )
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(null=True, max_length=50)

    def __str__(self):
        return f"{self.agent_name}"



# Create your models here.
class TicketStatus(models.TextChoices):
 TO_DO = 'To Do'
 IN_PROGRESS = 'In Progress'
 IN_REVIEW = 'In Review'
 DONE = 'Done'

class Ticket(models.Model):
 customer_name = models.CharField(max_length=100)
 assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
 status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
 subject = models.TextField()
 created_at = models.DateTimeField('created at', auto_now_add=True)
 updated_at = models.DateTimeField('updated at', auto_now=True)        
    