from ninja import ModelSchema

from vendor.models import Vendor


class VendorInSchema(ModelSchema):
    class Meta:
        model = Vendor
        fields = ["name", "contact_details", "address", "vendor_code"]
