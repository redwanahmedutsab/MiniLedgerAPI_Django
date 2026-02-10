from rest_framework.viewsets import ModelViewSet
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
