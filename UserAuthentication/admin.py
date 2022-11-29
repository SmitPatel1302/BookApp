from django.contrib import admin
from UserAuthentication.models import CustomUserAuthentication
from UserAuthentication.addressModel import UserAddress
from import_export.admin import ImportExportModelAdmin

@admin.register(CustomUserAuthentication,UserAddress)
class ViewAdmin(ImportExportModelAdmin):
    pass
