from django.db.models import Count
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from analysis.models import AnalysisTag, AnalysisEntry, QUALITATIVE
from analysis.serializers import AnalysisTagSerializer, AnalysisEntrySerializer, AnalysisEntryDetailSerializer
from analysis.services import get_qualitative_diagnosis
from ext.rest_framework.viewsets.dynamic_serializer import ActionBasedSerializerClassMixin
from ext.rest_framework.viewsets.mixins import ListRequiresFilterMixin


class AnalysisTagFilterSet(filters.FilterSet):
    class Meta:
        model = AnalysisTag
        fields = ['type']


class AnalysisTagViewSet(ListRequiresFilterMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = AnalysisTag.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AnalysisTagSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AnalysisTagFilterSet

    require_filter_by = ['type']


class AnalysisEntryViewSet(ActionBasedSerializerClassMixin, viewsets.ModelViewSet):
    queryset = AnalysisEntry.objects.all()
    permission_classes = [IsAuthenticated]

    serializer_class = AnalysisEntrySerializer
    retrieve_serializer_class = AnalysisEntryDetailSerializer

    def perform_create(self, serializer):
        obj: AnalysisEntry = serializer.save()
        if obj.type == QUALITATIVE:
            result = get_qualitative_diagnosis(obj)
            obj.diagnosis = result
            obj.save()


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(
            quantitative_analysis_entries_count=Count('quantitative_analysis_entries')
        ).order_by('-id')

