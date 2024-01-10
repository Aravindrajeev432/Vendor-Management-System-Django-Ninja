from django.shortcuts import render
from ninja import Router

from vendor.schemas import VendorInSchema
# Create your views here.



router = Router( )

@router.post('/')
def create_vendor(request, payload: VendorInSchema):
    return {}