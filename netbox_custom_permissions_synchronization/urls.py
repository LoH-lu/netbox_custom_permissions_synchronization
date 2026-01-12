from django.urls import path
from . import views

urlpatterns = [
    # Prefix -> IPs (+ VLAN)
    path("sync/prefix/<int:prefix_id>/", views.PrefixPermissionsSyncView.as_view(), name="prefix_permissions_sync"),

    # VM -> Interfaces + Virtual Disks
    path("sync/vm/<int:vm_id>/", views.VMPermissionsSyncView.as_view(), name="vm_permissions_sync"),
]