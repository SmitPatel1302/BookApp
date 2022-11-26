from django.contrib import admin
from contactus.models import ContactUs
from import_export.admin import ImportExportModelAdmin

@admin.register(ContactUs)
class ViewAdmin(ImportExportModelAdmin):
    pass
