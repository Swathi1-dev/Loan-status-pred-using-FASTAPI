from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_loan_status

#define input schema
class PredictionInput(BaseModel):
        Gender: int
        Married: int
        Dependents: int
        Education: int
        Self_Employed: int
        ApplicantIncome: int
        CoapplicantIncome: int
        LoanAmount: int
        Loan_Amount_Term: int
        Credit_History: int
        Property_Area: int
        
app=FastAPI(title="Loan status pred")
#ml prediciton endpoint

@app.post("/predict")
def predict_loan(input_data:PredictionInput):
    prediction=predict_loan_status(input_data.model_dump())
    return {
        "Prediction":int(prediction)
        
    }