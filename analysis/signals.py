from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from analysis.disease_prediction import get_disease_prediction
from analysis.models import AnalysisEntry, QuantitativeAnalysisEntry
from analysis.services import parse_quantitative_analysis_entries, get_qualitative_diagnosis


@receiver(post_save, sender=AnalysisEntry)
def fill_quantitative_analysis_entries(instance: AnalysisEntry, *_, **__):
    parse_quantitative_analysis_entries(instance)


@receiver(pre_save, sender=QuantitativeAnalysisEntry)
def diagnose_quantitative_analysis_entry(instance: QuantitativeAnalysisEntry, *_, **__):
    result = get_disease_prediction(instance)

    if result is None:
        return

    diagnosis, normal_value = result

    instance.diagnosis = diagnosis
    instance.normal_value = normal_value
