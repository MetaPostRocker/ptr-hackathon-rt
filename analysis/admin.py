from django.contrib import admin

from analysis.models import AnalysisTag, AnalysisEntry


@admin.register(AnalysisTag)
class AnalysisTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(AnalysisEntry)
class AnalysisEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner', 'tags_joined', 'owner', 'diagnosis')

    @admin.display(description='Tags')
    def tags_joined(self, obj: AnalysisEntry):
        return ', '.join(item.name for item in obj.tags.all())
