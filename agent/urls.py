from django.urls import path
from django.contrib import admin
from .views import *

app_name = 'agent'
urlpatterns = [
    path('' , agent_grid , name = 'agent-grid'),
    path('agent-single/' , agent_single , name='agent-single'),
]
