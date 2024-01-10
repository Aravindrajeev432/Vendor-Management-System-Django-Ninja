from django.contrib import admin

from purchase_and_performance.models import HistoricPerformance, PurchaseOrder

# Register your models here.

admin.site.register(PurchaseOrder)
admin.site.register(HistoricPerformance)