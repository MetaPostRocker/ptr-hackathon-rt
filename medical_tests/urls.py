from rest_framework.routers import SimpleRouter

from medical_tests.views import MedicalCertificateViewSet

medical_tests_router = SimpleRouter()

medical_tests_router.register('medical_certificates/medical_tests',
                              MedicalCertificateViewSet)
