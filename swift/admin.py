from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.SWIFTAccountDetail)
class SwiftAccountAdmin(admin.ModelAdmin):
    list_display = ["business_name", "business_address", "account_number"]
    search_fields = ["business_name", "account_number"]