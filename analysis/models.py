from colorfield.fields import ColorField
from django.db import models

from analysis.ml_models import PREDICTOR_CHOICES

QUANTITATIVE, QUALITATIVE = 'quantitative', 'qualitative'

ANALYSIS_TYPES = (
    (QUANTITATIVE, 'Quantitative'),
    (QUALITATIVE, 'Qualitative'),
)


class AnalysisTag(models.Model):
    name = models.CharField('Name', max_length=20)
    type = models.CharField('Type of Analysis', choices=ANALYSIS_TYPES, max_length=12)
    background_color = ColorField(verbose_name='Background Color', format='hexa', default='#FFFFFF00')
    text_color = ColorField(verbose_name='Text Color', format='hexa', default='#000000FF')
    processing_model = models.CharField('Choose model for processing', choices=PREDICTOR_CHOICES, null=True, blank=True,
                                        help_text='Leave empty if no suitable model available. '
                                                  'Does not work for type "Quantitative"', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class AnalysisEntry(models.Model):
    name = models.CharField('Analysis name', max_length=40)
    type = models.CharField('Type of Analysis', choices=ANALYSIS_TYPES, max_length=12)
    tags = models.ManyToManyField(verbose_name='Tags', to='analysis.AnalysisTag')
    analysis_date = models.DateField('Analysis date')
    file = models.FileField('File')
    owner = models.ForeignKey(verbose_name='Owner', to='users.User', on_delete=models.CASCADE)
    diagnosis = models.TextField(verbose_name='Diagnosis', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class QuantitativeAnalysisEntry(models.Model):
    analysis_entry = models.ForeignKey(verbose_name='Analysis entry', to='analysis.AnalysisEntry',
                                       on_delete=models.CASCADE, related_name='quantitative_analysis_entries')
    name = models.CharField('Name', max_length=40)
    value = models.FloatField('Value')
    unit = models.CharField('Unit', max_length=12, null=True, blank=True)
    normal_value = models.TextField('Normal value', null=True, blank=True)
