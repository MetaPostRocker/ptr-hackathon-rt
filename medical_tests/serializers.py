from django.utils import timezone
from rest_framework import serializers

from medical_tests.models import MedicalCertificate, MedicalCertificateType, Vaccine


# class MedicalCertificateTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicalCertificateType


class MedicalCertificateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    expired = serializers.SerializerMethodField()

    @staticmethod
    def get_expired(obj: MedicalCertificate):
        return obj.expiration_date < timezone.now()

    class Meta:
        model = MedicalCertificate
        fields = ('type', 'owner', 'file', 'given_by', 'created_date', 'received_date', 'expiration_date', 'expired')


class VaccineSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    expired = serializers.SerializerMethodField()

    @staticmethod
    def get_expired(obj: Vaccine):
        return obj.expiration_date < timezone.now()

    class Meta:
        model = Vaccine
        fields = ('type', 'owner', 'file', 'given_by', 'created_date', 'received_date', 'expiration_date', 'expired')
