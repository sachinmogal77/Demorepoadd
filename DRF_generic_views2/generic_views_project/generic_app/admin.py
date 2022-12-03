from django.contrib import admin
from .models import Bank
# Register your models here.

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display =['acc_holder_name','acc_no','acc_type']