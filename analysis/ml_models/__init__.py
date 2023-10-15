from analysis.ml_models.concrete import TrumorDetectionModel, PneumoniaDetectionModel

PREDICTOR_CHOICES = (
    ('trumor_detection', 'Trumor detection'),
    ('pneumonia_detection', 'Pneumonia detection')
)


PREDICTORS_MAP = {
    'trumor_detection': TrumorDetectionModel,
    'pneumonia_detection': PneumoniaDetectionModel,
}


def initialize_models():
    for item in PREDICTORS_MAP.values():
        item.initialize()
