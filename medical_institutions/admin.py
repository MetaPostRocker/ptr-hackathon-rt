from django.contrib import admin

from medical_institutions.models import MedicalInstitution


@admin.register(MedicalInstitution)
class MedicalInstitutionAdmin(admin.ModelAdmin):
    pass
