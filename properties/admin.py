from django.contrib import admin

from .models import (
    Property,
    Agent,
    Client,
    PropertyInquiry,
    PropertyTour,
)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'property_type',
        'price',
        'location',
        'status',
        'created_at',
    )

    list_filter = ('property_type', 'status')
    search_fields = ('title', 'location', 'description')
    ordering = ('-created_at',)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'agency_name',
        'license_number',
    )

    search_fields = ('full_name', 'email', 'phone')
    ordering = ('full_name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'created_at',
    )

    search_fields = ('full_name', 'email', 'phone')
    ordering = ('full_name',)


@admin.register(PropertyInquiry)
class PropertyInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'client_name',
        'email',
        'property',
        'status',
        'created_at',
    )

    list_filter = ('status', 'created_at')
    search_fields = ('client_name', 'email', 'phone')
    ordering = ('-created_at',)


@admin.register(PropertyTour)
class PropertyTourAdmin(admin.ModelAdmin):
    list_display = (
        'client_name',
        'email',
        'property',
        'scheduled_at',
        'status',
    )

    list_filter = ('status', 'scheduled_at')
    search_fields = ('client_name', 'email', 'phone')
    ordering = ('scheduled_at',)