from fastapi import APIRouter

from app.schemas import PredictIn
from app.services.ml import get_prediction

ml_router = APIRouter(prefix='/ml', tags=['ML-integration'])


@ml_router.post('/predict')
def predict(input_data: PredictIn):
    prediction = get_prediction(input_data)

    return {'prediction': prediction[0]}
