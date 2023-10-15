from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from analysis.models import AnalysisEntry
from analysis.services import parse_quantitative_analysis_entries, get_qualitative_diagnosis


@receiver(post_save, sender=AnalysisEntry)
def fill_quantitative_analysis_entries(instance: AnalysisEntry, *_, **__):
    parse_quantitative_analysis_entries(instance)


# @receiver(post_save, sender=AnalysisEntry)
# def get_qualitative_diagnosis_pre_save(instance: AnalysisEntry, *_, **__):
#     get_qualitative_diagnosis(instance)
