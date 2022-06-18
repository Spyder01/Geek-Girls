import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from services.Predict import get_model, predict
from services.get_message import get_message





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



#app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.post('/api/predict')
async def Predict_Response(query: Query):
    
    #prediction = predict(model, np.array("4 4 7 4 5 4 0 0 0 0 0 0 0 0 0 0 0".split (" ")).reshape (1, -1))
  try:
    res = get_message(query.query)
    return {
        "success": True,
        "data": {
            "query": res
        }
    }
  except Exception as e:
    return {
        "success": False,
        "data": {
            "error": str(e)
        }
    }



