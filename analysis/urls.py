from rest_framework.routers import SimpleRouter

from analysis.views import AnalysisTagViewSet, AnalysisEntryViewSet

analysis_router = SimpleRouter()

analysis_router.register('analysis/analysis_tags', AnalysisTagViewSet)
analysis_router.register('analysis/analysis_entries', AnalysisEntryViewSet)
