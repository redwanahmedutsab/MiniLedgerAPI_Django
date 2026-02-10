from django.urls import path
from .views import LedgerEntryView, CustomerSummaryView

urlpatterns = [
    path('customers/<int:customer_id>/entries/', LedgerEntryView.as_view()),
    path('customers/<int:customer_id>/summary/', CustomerSummaryView.as_view()),
]
