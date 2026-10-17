from django.db import models


class Property(models.Model):
    PROPERTY_TYPES = [
        ('HOUSE', 'House'),
        ('APARTMENT', 'Apartment'),
        ('LAND', 'Land'),
        ('COMMERCIAL', 'Commercial'),
    ]

    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('SOLD', 'Sold'),
        ('RENTED', 'Rented'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='properties/',
        blank=True,
        null=True
    )

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        default='HOUSE'
    )

    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    area_sqft = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AVAILABLE'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Agent(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    agency_name = models.CharField(
        max_length=150,
        blank=True
    )

    license_number = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Client(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class PropertyInquiry(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('CONTACTED', 'Contacted'),
        ('CLOSED', 'Closed'),
    ]

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='inquiries'
    )

    client_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NEW'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.property.title}"


class PropertyTour(models.Model):
    TOUR_STATUS = [
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='tours'
    )

    client_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    scheduled_at = models.DateTimeField()
    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=TOUR_STATUS,
        default='SCHEDULED'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.property.title}"