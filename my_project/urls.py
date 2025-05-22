from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/accounts-auth/", include("rest_framework.urls")),
    path("api/inventory/", include("inventory.urls")),
]
