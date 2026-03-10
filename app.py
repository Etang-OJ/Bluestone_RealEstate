from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "Output"

rental_model = joblib.load(MODEL_DIR / "rental_demand_model.joblib")
sales_model = joblib.load(MODEL_DIR / "sales_price_model.joblib")


class RentalRequest(BaseModel):
    LISTING_TYPE: str
    parsed_city: str
    parsed_state: str
    parsed_zip: str
    listing_month: int
    listing_quarter: int
    listing_year: int
    avg_lead_score: float
    avg_follow_up: float
    avg_response_time: float
    price_city_mean: float
    log_price: float
    log_price_per_day_on_market: float
    DAYS_ON_MARKET_capped: int
    price_vs_city_mean_capped: float
    inquiry_count_capped: int


class SalesRequest(BaseModel):
    CITY: str
    STATE: str
    ZIPCODE: int
    DAYS_TO_CLOSE: int
    MARKET_AVG_DOM: float
    PROPERTY_TYPE: str
    FINANCING_TYPE: str
    MARKET_AVG_PRICE: float
    EARNEST_MONEY_PCT: float
    TRANSACTION_TYPE: str
    CONTINGENCY_APPRAISAL: bool
    CONTINGENCY_FINANCING: bool
    CONTINGENCY_INSPECTION: bool
    inq_CHANNEL: str
    inq_CONVERTED: bool
    inq_LEAD_SCORE: int
    inq_FOLLOW_UP_COUNT: int
    inq_RESPONSE_TIME_HRS: float
    offer_month: int
    close_month: int
    days_offer_to_accept: int
    close_speed_vs_market: float
    inquiry_engagement: float
    log_price_vs_market: float


@app.get("/")
def home():
    return {"message": "Bluestone Real Estate ML API running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict/rental")
def predict_rental(payload: RentalRequest):
    df = pd.DataFrame([payload.model_dump()])
    pred = int(rental_model.predict(df)[0])
    prob = float(rental_model.predict_proba(df)[0, 1])

    return {
        "prediction": pred,
        "probability": prob
    }


@app.post("/predict/sales")
def predict_sales(payload: SalesRequest):
    row = payload.model_dump()
    row["inq_RESPONSE_TIME(HRS)"] = row.pop("inq_RESPONSE_TIME_HRS")

    df = pd.DataFrame([row])

    pred_log = float(sales_model.predict(df)[0])
    pred_price = float(np.expm1(pred_log))

    return {
        "predicted_log_price": pred_log,
        "predicted_price": pred_price
    }