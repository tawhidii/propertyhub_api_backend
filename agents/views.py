from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Agents
from .serializers import AgentsSerializers


class AgentsListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializers
    pagination_class = None


class AgentView(RetrieveAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializers


class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AgentsSerializers
    queryset = Agents.objects.filter(top_seller=True)
    pagination_class = None

