from rest_framework import serializers

from analysis.models import AnalysisTag, AnalysisEntry, QuantitativeAnalysisEntry


class AnalysisTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnalysisTag
        fields = ('url', 'name', 'background_color', 'text_color')


class QuantitativeAnalysisEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantitativeAnalysisEntry
        fields = ('name', 'value', 'unit')


class AnalysisEntrySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quantitative_analysis_entries_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = AnalysisEntry
        fields = ('url', 'name', 'type', 'tags', 'quantitative_analysis_entries_count', 'file',
                  'analysis_date', 'diagnosis', 'owner')
        extra_kwargs = {'diagnosis': {'read_only': True}}


class AnalysisEntryDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quantitative_analysis_entries = QuantitativeAnalysisEntrySerializer(many=True, read_only=True)

    class Meta:
        model = AnalysisEntry
        fields = ('url', 'name', 'type', 'tags', 'file', 'analysis_date',
                  'diagnosis', 'quantitative_analysis_entries', 'owner')
        extra_kwargs = {'diagnosis': {'read_only': True}}
