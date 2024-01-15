from typing import Type, Union, List, Any

from ninja import ModelSchema, Schema

from vendor.models import Vendor


class ErroSchema(Schema):
    detail: str

class VendorListOutSchema(ModelSchema):
    class Meta:
        model = Vendor
        fields = "__all__"


class VendorInSchema(ModelSchema):
    class Meta:
        model = Vendor
        fields = ["name", "contact_details", "address", "vendor_code"]


class VendorOutSchema(ModelSchema):
    class Meta:
        model = Vendor
        fields = ['id',"name", "contact_details", "address", "vendor_code"]
