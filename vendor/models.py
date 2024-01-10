from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    vendor_code = models.CharField(max_length=255, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    qulity_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
