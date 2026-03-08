import joblib

from app.schemas import PredictIn

model = joblib.load('ml/task_model.joblib')

def get_prediction(input_data: PredictIn):
    prediction = model.predict([input_data.description])

    return prediction