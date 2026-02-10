from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from .models import LedgerEntry
from .serializers import LedgerEntrySerializer
from customers.models import Customer


class LedgerEntryView(APIView):

    def get(self, request, customer_id):
        entries = LedgerEntry.objects.filter(
            customer__id=customer_id,
            customer__user=request.user
        )

        entry_type = request.query_params.get('type')
        if entry_type:
            entries = entries.filter(type=entry_type)

        start = request.query_params.get('start_date')
        end = request.query_params.get('end_date')
        if start and end:
            entries = entries.filter(entry_date__range=[start, end])

        serializer = LedgerEntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id, user=request.user)
        serializer = LedgerEntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=customer)
        return Response(serializer.data)


class CustomerSummaryView(APIView):

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id, user=request.user)
        entries = customer.entries.all()

        credit = entries.filter(type='credit').aggregate(
            total=Sum('amount'))['total'] or 0
        debit = entries.filter(type='debit').aggregate(
            total=Sum('amount'))['total'] or 0

        return Response({
            "total_credit": credit,
            "total_debit": debit,
            "balance": credit - debit
        })
