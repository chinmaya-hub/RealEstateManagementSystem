from django import forms
from django.utils import timezone

from .models import (
    PropertyInquiry,
    PropertyTour,
    Agent,
    Client,
)


class PropertyInquiryForm(forms.ModelForm):
    class Meta:
        model = PropertyInquiry

        fields = [
            'client_name',
            'email',
            'phone',
            'message',
        ]

        widgets = {
            'client_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number',
            }),
            'message': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your inquiry here...',
            }),
        }


class PropertyTourForm(forms.ModelForm):
    scheduled_at = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
        }),
        label='Preferred date and time',
    )

    class Meta:
        model = PropertyTour

        fields = [
            'client_name',
            'email',
            'phone',
            'scheduled_at',
            'notes',
        ]

        widgets = {
            'client_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number',
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Additional notes (optional)',
            }),
        }

    def clean_scheduled_at(self):
        scheduled_at = self.cleaned_data['scheduled_at']

        if timezone.is_naive(scheduled_at):
            scheduled_at = timezone.make_aware(
                scheduled_at,
                timezone.get_current_timezone()
            )

        if scheduled_at <= timezone.now():
            raise forms.ValidationError(
                'Please select a future date and time.'
            )

        return scheduled_at


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent

        fields = [
            'full_name',
            'email',
            'phone',
            'agency_name',
            'license_number',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter agent full name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter agent email',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter agent phone number',
            }),
            'agency_name': forms.TextInput(attrs={
                'placeholder': 'Enter agency name (optional)',
            }),
            'license_number': forms.TextInput(attrs={
                'placeholder': 'Enter license number (optional)',
            }),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = [
            'full_name',
            'email',
            'phone',
            'address',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter client full name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter client email',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter client phone number',
            }),
            'address': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Enter client address (optional)',
            }),
        }