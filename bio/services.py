import pickle
import pandas as pd
from .models import BloodTest
from sklearn.neural_network import MLPClassifier


class BloodTestService:

    def __init__(self):
        self.model: MLPClassifier = pickle.load(open('bio/learning-algorithms/nn-sgd.model', 'rb'))

    @staticmethod
    def model_to_df(test_model):
        params = {
            'Gender': (0, 1)[test_model.person.sex == 'male'],
            'AGE': test_model.person.age,
            'Urea': test_model.urea,
            'Cr': test_model.cr,
            'HbA1c': test_model.hba1c,
            'Chol': test_model.chol,
            'TG': test_model.tg,
            'HDL': test_model.hdl,
            'LDL': test_model.ldl,
            'VLDL': test_model.vldl,
            'BMI': test_model.person.weight / (test_model.person.height / 100) ** 2
        }
        return pd.DataFrame([params.values()], columns=params.keys())

    def predict(self, model: BloodTest):
        df = self.model_to_df(model)
        return self.model.predict(df)[0]
