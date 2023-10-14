from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from medical_tests.models import MedicalCertificate, Vaccine
from medical_tests.serializers import MedicalCertificateSerializer, VaccineSerializer


class MedicalCertificateViewSet(viewsets.ModelViewSet):
    queryset = MedicalCertificate.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MedicalCertificateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = VaccineSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)
