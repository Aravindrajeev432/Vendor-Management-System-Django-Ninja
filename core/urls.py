"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from ninja_jwt.routers.obtain import obtain_pair_router

from vendor.views import router as vendor_router
api = NinjaAPI()
api.add_router("/token", tags=["Auth"], router=obtain_pair_router)
api.add_router('/vendors/', tags=['Vendor'], router=vendor_router)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    
]
