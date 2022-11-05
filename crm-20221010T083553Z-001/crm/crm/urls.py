"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path, include
from leads.views import LandingPageView,registerPage ,loginPage , logoutUser 
from agents.views import  dashboard , agentdashboard,index,ticket_by_id,add_Ticket,update_Ticket,delete_Ticket




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView, name='landing-page'),
    path('dashboard/', dashboard , name='dashboard'),
    path('agentdashboard/', agentdashboard , name='agent-dashboard'),
    path('leads/', include(('leads.urls','leads'),namespace="leads")),
    path('agents/',include(('agents.urls','agents'),namespace="agents")),
    path('signup/',registerPage, name='signup'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutUser,name='logout'),
    path('index/', index, name='index'),
    path('ticket/<int:ticket_id>', ticket_by_id, name='ticket_by_id'),
    path('getData',add_Ticket,name='add_ticket'),
    path('updateTicket/<ticket_id>',update_Ticket, name='update'),
    path('deleteTicket/<ticket_id>',delete_Ticket, name='delete'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

