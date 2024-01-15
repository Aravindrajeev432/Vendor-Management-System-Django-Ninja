import asyncio
import time
from typing import List
from django.shortcuts import get_object_or_404, render
from ninja import Router
from ninja.orm import create_schema
from django.http import HttpRequest, HttpResponse
from purchase_and_performance.models import PurchaseOrder

# from icecream import ic


from vendor import schemas
from vendor.models import Vendor

# Create your views here.


router = Router()


@router.post("/", response={201: schemas.VendorOutSchema, 400: schemas.ErroSchema})
def create_purchase_order(request: HttpRequest, payload: schemas.VendorInSchema):
    try:
        vendor = PurchaseOrder.objects.create(**payload.dict())
    except Exception as e:
        return 400, {"message": str(e)}
    return 201, vendor

@router.get('/', response=List[schemas.VendorListOutSchema])
def list_purchase_orders(request: HttpRequest):
    
    vendors = PurchaseOrder.objects.all()
    return vendors

@router.get('/{po_id}', response={200:schemas.VendorListOutSchema,404:schemas.ErroSchema})
def get_purchase_order(request: HttpRequest, po_id: int):
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)
    return purchase_order

@router.put('/{po_id}', response={200:schemas.VendorListOutSchema,404:schemas.ErroSchema})
def update_purchase_order(request: HttpRequest, po_id: int, payload: schemas.VendorInSchema):
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)
    for attr, value in payload.dict().items():
        setattr(purchase_order, attr, value)
    purchase_order.save()
    return purchase_order

@router.delete('/{po_id}')
def delete_purchase_order(request: HttpRequest, po_id: int):
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)
    purchase_order.delete()
    return purchase_order
