from django.contrib import admin
from .models import LedgerEntry

@admin.register(LedgerEntry)
class LedgerEntryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'type',
        'amount',
        'entry_date'
    )
    list_filter = ('type', 'entry_date')
    search_fields = ('customer__name',)