import cv2
import numpy as np
from PIL import Image
from django.conf import settings

from analysis.ml_models.base import BaseKerasModel


class TrumorDetectionModel(BaseKerasModel):
    model_path = settings.BASE_DIR / 'analysis' / 'ml_models' / 'models' / 'mri_predict_model.h5'

    @classmethod
    def predict(cls, filepath):
        if cls.model is None:
            raise ValueError('Model is not initialized')

        image = Image.open(filepath)
        opencvImage = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img = cv2.resize(opencvImage, (150, 150))
        img = img.reshape(1, 150, 150, 3)
        p = cls.model.predict(img)
        p = np.argmax(p, axis=1)[0]

        if p == 0:
            return 'Рак (Глиома)'
        elif p == 1:
            return 'Здоров'
        elif p == 2:
            return 'Рак (Менингиома)'
        else:
            return 'Опухоль Гипофиза'


class PneumoniaDetectionModel(BaseKerasModel):
    model_path = settings.BASE_DIR / 'analysis' / 'ml_models' / 'models' / 'pneumonia_detection_cnn.h5'

    @classmethod
    def predict(cls, filepath):
        if cls.model is None:
            raise ValueError('Model is not initialized')

        img = Image.open(filepath)
        opencvImage = np.array(img) / 255
        img = cv2.resize(opencvImage, (150, 150))
        img = img.reshape(1, 150, 150, 1)
        p = cls.model.predict(img)
        result = 'Здоров' if p[0][0] > 0.5 else 'Пневмония'
        return result
