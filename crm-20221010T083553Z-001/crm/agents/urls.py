
from django.urls import URLPattern

from django.urls import path
from .views import  AgentCreateView , agent_list , agentdetail

app_name = 'agents'

urlpatterns = [
    path('', agent_list , name='agent-list'),
    path('<int:pk>/', agentdetail, name='agent-detail'),
    # path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
#    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='Agent-delete'),
    path('create/',AgentCreateView, name='agent-create')
]

