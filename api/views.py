from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import CreditSerializer
from credit.models import Borrower


class CreditViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Borrower.objects.all().order_by('iin')
    serializer_class = CreditSerializer
    permission_classes = [permissions.IsAuthenticated]

