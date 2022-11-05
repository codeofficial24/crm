from django.urls import path
from .views import (
     lead_list, lead_detail,lead_create,lead_update,lead_create,lead_update , lead_delete 
)
from .helpers.pdf import GeneratePdf ,helper
from .helpers.email import  send_my_mail

from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

app_names = "leads"

urlpatterns = [
    path('', lead_list, name='lead-list'),
    path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/genratequoation/',GeneratePdf.as_view(), name='pdf'),
    path('<int:pk>/helper/', helper , name='help'),
    path('<int:pk>/delete/', lead_delete , name='lead-delete'),
    path('<int:pk>/email', send_my_mail, name='sendEmail'),
    path('create/',lead_create, name='lead-create'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT)