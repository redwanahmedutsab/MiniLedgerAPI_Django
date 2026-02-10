from django.db import models
from customers.models import Customer


class LedgerEntry(models.Model):
    TYPE_CHOICES = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='entries')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)
    entry_date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.amount}"
