from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Land(models.Model):

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name="lands"
    )

    location = models.CharField(max_length=200)

    district = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    area_acres = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    soil_type = models.CharField(
        max_length=100
    )

    land_photo = models.ImageField(
        upload_to="land_photos/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.farmer.name} - {self.location}"


class Crop(models.Model):

    land = models.ForeignKey(
        Land,
        on_delete=models.CASCADE,
        related_name="crops"
    )

    crop_name = models.CharField(
        max_length=100
    )

    variety = models.CharField(
        max_length=100,
        blank=True
    )

    cultivation_area = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    expected_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    expected_harvest_date = models.DateField()

    expected_selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.crop_name} - {self.land.farmer.name}"
class Investor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class InvestmentRequest(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        related_name="investment_requests"
    )

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="investment_requests"
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.investor.name} → {self.crop.crop_name} ({self.status})"
    

class Notification(models.Model):

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    investment_request = models.ForeignKey(
        InvestmentRequest,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notifications"
    )

    title = models.CharField(max_length=150)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.recipient.username}"
