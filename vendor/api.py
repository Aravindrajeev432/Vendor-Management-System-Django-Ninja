import asyncio
import time
from typing import List
from django.shortcuts import get_object_or_404, render
from ninja import Router
from ninja.orm import create_schema
from django.http import HttpRequest, HttpResponse

# from icecream import ic


from vendor import schemas
from vendor.models import Vendor

# Create your views here.


router = Router()


@router.post("/", response={201: schemas.VendorOutSchema, 400: schemas.ErroSchema})
def create_vendor(request: HttpRequest, payload: schemas.VendorInSchema):
    try:
        vendor = Vendor.objects.create(**payload.dict())
    except Exception as e:
        return 400, {"message": str(e)}
    return 201, vendor

# @router.get('/', response=List[schemas.VendorListOutSchema])
# def list_vendors(request: HttpRequest):
#     time.sleep(3)
#     vendors = Vendor.objects.all()
#     return vendors


@router.get('/', response=List[schemas.VendorListOutSchema])
async def list_vendors(request: HttpRequest):
    asyncio.sleep(3)
    vendors = [v async for v in Vendor.objects.all()]
    return vendors

@router.get('/{vendor_id}', response={200:schemas.VendorListOutSchema,404:schemas.ErroSchema})
def get_vendor(request: HttpRequest, vendor_id: int):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    return vendor


@router.put('/{vendor_id}', response={200:schemas.VendorListOutSchema,404:schemas.ErroSchema})
def update_vendor(request: HttpRequest, vendor_id: int, payload: schemas.VendorInSchema):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return vendor