from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from services.Predict import get_model, predict


app = FastAPI()


origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers
)


class Query(BaseModel):
    query: str


@app.get('/')
async def Index():
    return {"message": "Hello World"}


@app.post('/api/predict')
async def Predict_Response(query: Query):
    model = get_model()
    return {
        "success": True,
        "data": {
            predict(model, query.query)
        }
    }
