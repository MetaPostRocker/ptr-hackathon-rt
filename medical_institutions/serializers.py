from rest_framework import serializers

from medical_institutions.models import MedicalInstitution


class MedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = '__all__'
