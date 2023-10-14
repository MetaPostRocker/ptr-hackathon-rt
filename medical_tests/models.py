from django.conf import settings
from django.db import models


class MedicalCertificateType(models.Model):
    name = models.CharField('Name', max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class VaccineType(models.Model):
    name = models.CharField('Name', max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class MedicalCertificate(models.Model):
    @staticmethod
    def user_directory_path(instance, filename):
        user_id = str(instance.owner.id)
        ext = filename.split('.')[-1]
        return settings.MEDIA_ROOT / 'medical_certificates' / f'user_{user_id}' / f'{filename}.{ext}'

    type = models.ForeignKey(verbose_name='Certificate type', to='medical_tests.MedicalCertificateType',
                             on_delete=models.CASCADE)
    file = models.FileField('File', upload_to=user_directory_path)
    owner = models.ForeignKey(verbose_name='Owner', to='users.User', on_delete=models.CASCADE)
    given_by = models.ForeignKey(verbose_name='Given by', to='medical_institutions.MedicalInstitution',
                                 on_delete=models.RESTRICT)
    created_date = models.DateTimeField('Date of creation', auto_now_add=True)
    received_date = models.DateTimeField('Received date')
    expiration_date = models.DateTimeField('Expiration date')

    def __str__(self):
        return f'{self.type.name} of {self.owner.get_full_name()}'

    class Meta:
        order_with_respect_to = 'owner'


class Vaccine(models.Model):
    @staticmethod
    def user_directory_path(instance, filename):
        user_id = str(instance.owner.id)
        ext = filename.split('.')[-1]
        return settings.MEDIA_ROOT / 'vaccines' / f'user_{user_id}' / f'{filename}.{ext}'

    type = models.ForeignKey(verbose_name='Vaccine type', to='medical_tests.VaccineType',
                             on_delete=models.CASCADE)
    file = models.FileField('File', upload_to=user_directory_path)
    owner = models.ForeignKey(verbose_name='Owner', to='users.User', on_delete=models.CASCADE)
    given_by = models.ForeignKey(verbose_name='Given by', to='medical_institutions.MedicalInstitution',
                                 on_delete=models.RESTRICT)
    created_date = models.DateTimeField('Date of creation', auto_now_add=True)
    received_date = models.DateTimeField('Received date')
    expiration_date = models.DateTimeField('Expiration date')

    def __str__(self):
        return f'{self.type.name} of {self.owner.get_full_name()}'

    class Meta:
        order_with_respect_to = 'owner'

