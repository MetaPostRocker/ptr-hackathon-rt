from rest_framework.routers import SimpleRouter

from medical_tests.views import MedicalCertificateViewSet, VaccineViewSet

medical_tests_router = SimpleRouter()

medical_tests_router.register('medical_tests/medical_certificates',
                              MedicalCertificateViewSet)
medical_tests_router.register('medical_tests/vaccines',
                              VaccineViewSet)
