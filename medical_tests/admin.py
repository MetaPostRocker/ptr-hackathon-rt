from django.contrib import admin

from medical_tests.models import MedicalCertificateType, MedicalCertificate


@admin.register(MedicalCertificateType)
class MedicalCertificateTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicalCertificate)
class MedicalCertificateAdmin(admin.ModelAdmin):
    pass
