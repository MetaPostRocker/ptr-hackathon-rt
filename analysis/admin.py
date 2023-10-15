from django.contrib import admin

from analysis.models import AnalysisTag


@admin.register(AnalysisTag)
class AnalysisTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
