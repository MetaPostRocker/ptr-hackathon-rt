from tensorflow import keras


class BaseKerasModel:
    model_path = None
    model = None

    @classmethod
    def initialize(cls):
        if cls.model_path is None:
            raise NotImplementedError('set model_path')

        cls.model = keras.models.load_model(cls.model_path)
