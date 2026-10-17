from django.urls import path

from . import views


urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Property Management
    path(
        'properties/',
        views.property_list,
        name='property_list'
    ),
    path(
        'properties/<int:pk>/',
        views.property_detail,
        name='property_detail'
    ),

    # Agent Management
    path(
        'agents/',
        views.agent_list,
        name='agent_list'
    ),
    path(
        'agents/add/',
        views.agent_create,
        name='agent_create'
    ),
    path(
        'agents/<int:pk>/edit/',
        views.agent_edit,
        name='agent_edit'
    ),
    path(
        'agents/<int:pk>/delete/',
        views.agent_delete,
        name='agent_delete'
    ),

    # Client Management
    path(
        'clients/',
        views.client_list,
        name='client_list'
    ),
    path(
        'clients/add/',
        views.client_create,
        name='client_create'
    ),
    path(
        'clients/<int:pk>/edit/',
        views.client_edit,
        name='client_edit'
    ),
    path(
        'clients/<int:pk>/delete/',
        views.client_delete,
        name='client_delete'
    ),
]