from django.contrib import admin

from medical_tests.models import MedicalCertificateType, MedicalCertificate, Vaccine, VaccineType


@admin.register(MedicalCertificateType)
class MedicalCertificateTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(VaccineType)
class VaccineTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicalCertificate)
class MedicalCertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass