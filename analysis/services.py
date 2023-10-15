from analysis.ml_models import PREDICTORS_MAP
from analysis.models import AnalysisEntry, QUANTITATIVE, QUALITATIVE, QuantitativeAnalysisEntry, AnalysisTag
from analysis.parsio_api import parse_pdf


mapping = {
    'ЕдИзм': 'unit',
    'Наименование анализа': 'name',
    'Норма': 'normal_value',
    'Результат': 'value'
}


def _map_data(data: list[dict]) -> list[dict]:
    return [{mapping[key]: val
            for key, val in item.items()}
            for item in data]


def parse_quantitative_analysis_entries(analysis_entry: AnalysisEntry):
    if analysis_entry.type == QUANTITATIVE and not analysis_entry.quantitative_analysis_entries.exists():
        data = parse_pdf(analysis_entry.file.path)
        data = _map_data(data)
        for item in data:
            item.pop('normal_value')
            QuantitativeAnalysisEntry.objects.create(analysis_entry=analysis_entry, **item)


def get_qualitative_diagnosis(analysis_entry: AnalysisEntry):

    if analysis_entry.type != QUALITATIVE:
        raise ValueError('Only qualitative entries are acceptable')

    tag: AnalysisTag = analysis_entry.tags.first()
    model = PREDICTORS_MAP[tag.processing_model]
    result = model.predict(analysis_entry.file.path)
    print(result)
    return result
