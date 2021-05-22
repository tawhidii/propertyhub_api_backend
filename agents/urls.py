from django.urls import path
from .views import AgentView, AgentsListView, TopSellerView

urlpatterns = [
    path('', AgentsListView.as_view()),
    path('topseller/', TopSellerView.as_view()),
    path('<pk>/', AgentView.as_view())
]
