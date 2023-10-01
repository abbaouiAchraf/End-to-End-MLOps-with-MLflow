import joblib
import pandas as pd
import numpy as np
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts/model_trainer/model.joblib")
    
    def prediction(self, data):
        prediction = self.model.predict(data)
        
        return prediction