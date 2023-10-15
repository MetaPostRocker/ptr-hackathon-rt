from analysis.models import QuantitativeAnalysisEntry

reference_values = {
    "Свободный Т3 (Трийодтиронин св.)": (
        0.9, 2.8, ["зоб"]
    ),
    "АТ-ТГ Антитела к Тиреоглобулину": (
        0, 40, ['Дифузный Интоксический Зоб']
    ),
    "Свободный Т4 (Тироксин св.)": (
        5, 12, ["зоб"]
    ),
    "ТТГ Тиреотропный гормон (III-поколения)": (
        0.23, 4.9, ["зоб"]
    ),
    "глюкоза": (
        3.8, 5.83, ["сахарный диабет"]
    ),
    "гликированный гемоглобин": (
        0, 6, ["сахарный диабет"]
    ),
    "щф": (
        37, 150, ["цирроз печени"]
    ),
    "ггт": (
        0, 55, ["цирроз печени"]
    ),
}


def get_disease_prediction(analysis_entry: QuantitativeAnalysisEntry):
    print(analysis_entry.name, analysis_entry.name in reference_values)
    if analysis_entry.name not in reference_values:
        return None

    reference = reference_values[analysis_entry.name]
    if float(analysis_entry.value) < reference[0] or float(analysis_entry.value) > reference[1]:
        print(reference)
        return reference[2][0], f'{reference[0]} - {reference[1]}'
