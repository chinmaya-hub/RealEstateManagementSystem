from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Q
from django.utils import timezone

from .models import (
    Property,
    Agent,
    Client,
    PropertyInquiry,
    PropertyTour,
)

from .forms import (
    PropertyInquiryForm,
    PropertyTourForm,
    AgentForm,
    ClientForm,
)


# =========================================================
# DASHBOARD
# =========================================================

def dashboard(request):
    property_type_stats = []

    for value, label in Property.PROPERTY_TYPES:
        property_type_stats.append({
            'label': label,
            'count': Property.objects.filter(
                property_type=value
            ).count(),
        })

    status_stats = []

    for value, label in Property.STATUS_CHOICES:
        status_stats.append({
            'label': label,
            'count': Property.objects.filter(
                status=value
            ).count(),
        })

    context = {
        'total_properties': Property.objects.count(),

        'available_properties': Property.objects.filter(
            status='AVAILABLE'
        ).count(),

        'total_agents': Agent.objects.count(),

        'total_clients': Client.objects.count(),

        'new_inquiries': PropertyInquiry.objects.filter(
            status='NEW'
        ).count(),

        'scheduled_tours': PropertyTour.objects.filter(
            status='SCHEDULED'
        ).count(),

        'recent_properties': Property.objects.order_by(
            '-created_at'
        )[:6],

        'recent_inquiries': PropertyInquiry.objects.select_related(
            'property'
        ).order_by('-created_at')[:5],

        'upcoming_tours': PropertyTour.objects.select_related(
            'property'
        ).filter(
            status='SCHEDULED',
            scheduled_at__gte=timezone.now()
        ).order_by('scheduled_at')[:5],

        'property_type_stats': property_type_stats,
        'status_stats': status_stats,

        'available_property_value': (
            Property.objects.filter(
                status='AVAILABLE'
            ).aggregate(total=Sum('price'))['total'] or 0
        ),
    }

    return render(
        request,
        'properties/dashboard.html',
        context
    )


# =========================================================
# PROPERTY LIST
# =========================================================

def property_list(request):
    properties = Property.objects.all().order_by('-created_at')

    search_query = request.GET.get('q', '').strip()
    selected_type = request.GET.get('type', '')
    selected_status = request.GET.get('status', '')

    if search_query:
        properties = properties.filter(
            Q(title__icontains=search_query)
            | Q(location__icontains=search_query)
            | Q(description__icontains=search_query)
        )

    valid_types = [
        value for value, label in Property.PROPERTY_TYPES
    ]

    valid_statuses = [
        value for value, label in Property.STATUS_CHOICES
    ]

    if selected_type in valid_types:
        properties = properties.filter(
            property_type=selected_type
        )

    if selected_status in valid_statuses:
        properties = properties.filter(
            status=selected_status
        )

    context = {
        'properties': properties,
        'search_query': search_query,
        'selected_type': selected_type,
        'selected_status': selected_status,
        'property_types': Property.PROPERTY_TYPES,
        'status_choices': Property.STATUS_CHOICES,
    }

    return render(
        request,
        'properties/property_list.html',
        context
    )


# =========================================================
# PROPERTY DETAILS, INQUIRY AND TOUR BOOKING
# =========================================================

def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)

    inquiry_form = PropertyInquiryForm()
    tour_form = PropertyTourForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'inquiry':
            inquiry_form = PropertyInquiryForm(request.POST)

            if inquiry_form.is_valid():
                inquiry = inquiry_form.save(commit=False)
                inquiry.property = property_obj
                inquiry.save()

                messages.success(
                    request,
                    'Your property inquiry was submitted successfully.'
                )

                return redirect(
                    'property_detail',
                    pk=property_obj.pk
                )

        elif form_type == 'tour':
            tour_form = PropertyTourForm(request.POST)

            if tour_form.is_valid():
                tour = tour_form.save(commit=False)
                tour.property = property_obj
                tour.save()

                messages.success(
                    request,
                    'Your property tour request was submitted successfully.'
                )

                return redirect(
                    'property_detail',
                    pk=property_obj.pk
                )

        else:
            messages.error(
                request,
                'Invalid form submission. Please try again.'
            )

    context = {
        'property': property_obj,
        'inquiry_form': inquiry_form,
        'tour_form': tour_form,
    }

    return render(
        request,
        'properties/property_detail.html',
        context
    )


# =========================================================
# AGENT MANAGEMENT
# Only authorized staff can access these pages.
# =========================================================

@staff_member_required(login_url='admin:login')
def agent_list(request):
    agents = Agent.objects.all().order_by('full_name')

    context = {
        'agents': agents,
    }

    return render(
        request,
        'properties/agent_list.html',
        context
    )


@staff_member_required(login_url='admin:login')
def agent_create(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Agent added successfully.'
            )

            return redirect('agent_list')
    else:
        form = AgentForm()

    context = {
        'form': form,
        'page_title': 'Add Agent',
        'button_text': 'Save Agent',
    }

    return render(
        request,
        'properties/agent_form.html',
        context
    )


@staff_member_required(login_url='admin:login')
def agent_edit(request, pk):
    agent = get_object_or_404(Agent, pk=pk)

    if request.method == 'POST':
        form = AgentForm(request.POST, instance=agent)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Agent updated successfully.'
            )

            return redirect('agent_list')
    else:
        form = AgentForm(instance=agent)

    context = {
        'form': form,
        'agent': agent,
        'page_title': 'Edit Agent',
        'button_text': 'Update Agent',
    }

    return render(
        request,
        'properties/agent_form.html',
        context
    )


@staff_member_required(login_url='admin:login')
def agent_delete(request, pk):
    agent = get_object_or_404(Agent, pk=pk)

    if request.method == 'POST':
        agent.delete()

        messages.success(
            request,
            'Agent deleted successfully.'
        )

        return redirect('agent_list')

    context = {
        'agent': agent,
    }

    return render(
        request,
        'properties/agent_confirm_delete.html',
        context
    )


# =========================================================
# CLIENT MANAGEMENT
# Only authorized staff can access these pages.
# =========================================================

@staff_member_required(login_url='admin:login')
def client_list(request):
    clients = Client.objects.all().order_by('full_name')

    context = {
        'clients': clients,
    }

    return render(
        request,
        'properties/client_list.html',
        context
    )


@staff_member_required(login_url='admin:login')
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Client added successfully.'
            )

            return redirect('client_list')
    else:
        form = ClientForm()

    context = {
        'form': form,
        'page_title': 'Add Client',
        'button_text': 'Save Client',
    }

    return render(
        request,
        'properties/client_form.html',
        context
    )


@staff_member_required(login_url='admin:login')
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Client updated successfully.'
            )

            return redirect('client_list')
    else:
        form = ClientForm(instance=client)

    context = {
        'form': form,
        'client': client,
        'page_title': 'Edit Client',
        'button_text': 'Update Client',
    }

    return render(
        request,
        'properties/client_form.html',
        context
    )


@staff_member_required(login_url='admin:login')
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        client.delete()

        messages.success(
            request,
            'Client deleted successfully.'
        )

        return redirect('client_list')

    context = {
        'client': client,
    }

    return render(
        request,
        'properties/client_confirm_delete.html',
        context
    )