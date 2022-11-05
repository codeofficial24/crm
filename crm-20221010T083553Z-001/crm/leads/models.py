from django.db import models
from django.db.models.signals import post_save, pre_save
from datetime import datetime
from agents.models import agent


class catagory(models.Model):
    catagory_name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.catagory_name}"


class product(models.Model):
    catagory = models.ForeignKey("catagory", on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 30 )
    price = models.CharField(max_length=30, default = "100")
    # @property
    # def price(self):
    #     return self.price

    def __str__(self):
        return f"{self.product_name}"


class Lead(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    size = models.CharField(max_length= 10, null= True)
    location = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length= 10)
    designation = models.CharField(max_length= 30,null= True)
    email = models.EmailField(max_length= 30,null= True)
    source = models.CharField(max_length= 20)
    stage = models.CharField(max_length= 20,default= "New")
    status = models.CharField(max_length= 20,null= True)
    pincode = models.CharField(max_length= 20,null= True)
    agent = models.ForeignKey(agent,on_delete= models.SET_NULL,  null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey("product",on_delete= models.SET_NULL,  null=True)
    #organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

            
    def __str__(self):

        return f"{self.id}"

class lead_communication(models.Model):
    lead_id = models.ForeignKey("Lead",on_delete=models.CASCADE)
    message = models.CharField(max_length= 500)
    Date_created = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    Type = models.CharField(max_length= 50 , null=True)
    proablity = models.IntegerField( default= 0 ,  null=True)

    
    def __str__(Lead):
        return f"Lead : {Lead.lead_id} "



# after customer agrees for demo
class lead_activity(models.Model):
    ACTIVITY_CHOICES =(
    ('Demo',"Demo"),
    ('Follow Up',"Follow Up"),
    ('Instalation',"Instalation")
    )
    STATUS_CHOICES =(
    ('1',"Pending"),
    ('3',"Completed")
    )
    lead_id = models.ForeignKey("Lead",on_delete=models.CASCADE)
    activity_name = models.CharField(max_length = 20,choices=ACTIVITY_CHOICES, default = '1')
    scheduled_date = models.DateField()
    actual_date = models.DateField(null=True)
    Date_created = models.DateField(auto_now_add=True)
    demo_status = models.CharField(max_length= 10,choices=STATUS_CHOICES, default = '1')


    def __str__(self):
        return f"{self.lead_id}"

# after lead converts to Customer
class Customer(models.Model):
    lead_id = models.ForeignKey("Lead",on_delete=models.CASCADE)
    org_name = models.CharField(max_length= 50)
    contact_name= models.CharField(max_length= 50)
    phone_number = models.CharField(max_length= 10)
    email = models.EmailField(max_length= 50,null= True) 
    conversation_date = models.DateField()
    renewal_date = models.DateField()
    start_date = models.DateField()
    subscription_used_date = models.DateField(max_length= 10)
    payment_cycle = models.CharField(max_length= 10)
    gst_no = models.CharField(max_length= 50)

    def __str__(self):
        return f"{self.org_name}"



class quotation(models.Model):
    lead_id = models.ForeignKey("Lead",on_delete=models.CASCADE)
    quotation_file_name = models.CharField(max_length = 30)
    Quantity = models.CharField(max_length = 30 )
    product_id = models.ForeignKey("product",on_delete= models.SET_NULL,  null=True)
    price_offered = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.lead_id}"

    # def __init__(self, *args, **kwargs):
    #     super(quotation, self).__init__(*args, **kwargs)
    #     self.set_price()

    # def save(self, *args, **kwargs):
    #     self.set_price()
    #     super(quotation, self).save(*args, **kwargs)

    # def set_default_price(self):
    #     if self.product_id and not self.price_offered:
    #         self.price_offered = self.product_id.price

