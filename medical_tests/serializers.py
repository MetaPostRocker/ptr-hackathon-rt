from pathlib import Path

from django.utils import timezone
from rest_framework import serializers

from medical_institutions.serializers import MedicalInstitutionSerializer
from medical_tests.models import MedicalCertificate, MedicalCertificateType, Vaccine, VaccineType


class MedicalCertificateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCertificateType
        fields = '__all__'


class VaccineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineType
        fields = '__all__'


class MedicalCertificateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    expired = serializers.SerializerMethodField()
    given_by = MedicalInstitutionSerializer()
    type = MedicalCertificateTypeSerializer()

    title = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    def get_display_image(self, obj: MedicalCertificate):
        return Path(obj.file.path).suffix.lower() in ('.png', '.jpg', '.jpeg')

    def get_title(self, obj: MedicalCertificate):
        return obj.type.name

    @staticmethod
    def get_expired(obj: MedicalCertificate):
        return obj.expiration_date < timezone.now()

    class Meta:
        model = MedicalCertificate
        fields = ('id', 'type', 'title', 'owner', 'file', 'given_by', 'created_date', 'received_date', 'expiration_date',
                  'expired', 'display_image')


class VaccineSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    expired = serializers.SerializerMethodField()
    type = VaccineTypeSerializer()

    title = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    def get_display_image(self, obj: MedicalCertificate):
        return Path(obj.file.path).suffix.lower() in ('.png', '.jpg', '.jpeg')

    def get_title(self, obj: MedicalCertificate):
        return obj.type.name

    @staticmethod
    def get_expired(obj: Vaccine):
        return obj.expiration_date < timezone.now()

    class Meta:
        model = Vaccine
        fields = ('id', 'type', 'title', 'owner', 'file', 'given_by', 'created_date', 'received_date', 'expiration_date',
                  'expired', 'display_image')
