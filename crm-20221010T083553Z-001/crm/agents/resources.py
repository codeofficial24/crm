from import_export import resources
from .models import agent

class AgentResource(resources.ModelResource):
    class Meta:
        model = agent