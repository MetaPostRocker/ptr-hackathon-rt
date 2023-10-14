from django.db import models


class MedicalInstitution(models.Model):
    title = models.CharField('Title', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
