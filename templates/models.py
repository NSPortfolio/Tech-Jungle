from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pickup_area = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Category(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    NEW_CONDITION = "New Condition"
    GOOD_CONDITION = "Good Condition"
    USED_CONDITION = "Used Condition"
    POOR_CONDITION = "Poor Condition"
    CONDITION = (
        (NEW_CONDITION, "New Condition"),
        (GOOD_CONDITION, "Good Condition"),
        (USED_CONDITION, "Used Condition"),
        (POOR_CONDITION, "Poor Condition"),
    )
    pickuponly = "Pick Up Only"
    shiponly = "Shipping Only"
    bothpickship = "Both Pick Up and Shipping"
    pick_ship = (
        (pickuponly, "Pick Up Only"),
        (shiponly, "Shipping Only"),
        (bothpickship, "Both Pick Up and Shipping"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, blank=True)
    name_of_product = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    condition = models.CharField(max_length=20, choices=CONDITION, default=GOOD_CONDITION)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    pickuporship = models.CharField(max_length=36, choices=pick_ship, default=pickuponly)
    photo = models.ImageField(upload_to='photos/')
    city = models.CharField(max_length=255, blank=True, null=True)
    saved = models.ManyToManyField(User, related_name='saved', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_of_product