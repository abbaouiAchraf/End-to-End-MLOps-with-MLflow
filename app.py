from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from MLOpsProject.pipeline.prediction import PredictionPipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler

app = Flask(__name__)

class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def categorical_columns(self):
        # Replace with your logic to get categorical columns
        return ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

    def encoding(self):
        categorical_columns = self.categorical_columns()
        label = LabelEncoder()
        for i in categorical_columns:
            self.data[i] = label.fit_transform(self.data[i])

    def feature_scaling(self):
        scaler = StandardScaler()  # Replace with your target column name
        self.data = scaler.fit_transform(self.data)


@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def trainPage():
    os.system("python main.py")
    return "Training Done"

@app.route('/predict', methods=['GET','POST'])
def index():
    if request.method == "POST":
        # Retrieve input data from the form
        age = float(request.form['age'])
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        default = request.form['default']
        balance = float(request.form['balance'])
        housing = request.form['housing']
        loan = request.form['loan']
        contact = request.form['contact']
        day = float(request.form['day'])
        month = request.form['month']
        duration = float(request.form['duration'])
        campaign = float(request.form['campaign'])
        pdays = float(request.form['pdays'])
        previous = float(request.form['previous'])
        poutcome = request.form['poutcome']

        # Create a DataFrame from the input data
        input_data = pd.DataFrame({
            'age': [age],
            'job': [job],
            'marital': [marital],
            'education': [education],
            'default': [default],
            'balance': [balance],
            'housing': [housing],
            'loan': [loan],
            'contact': [contact],
            'day': [day],
            'month': [month],
            'duration': [duration],
            'campaign': [campaign],
            'pdays': [pdays],
            'previous': [previous],
            'poutcome': [poutcome]
        })

        preprocessor = DataPreprocessor(input_data)
        preprocessor.encoding()
        preprocessor.feature_scaling()

        prediction_pipeline = PredictionPipeline()
        predictions = prediction_pipeline.prediction(input_data)

        return f'Predicted result: {predictions}'


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080",debug=True)