from tensorflow.keras.models import load_model

def get_model (path="models/model.h5"):
    model = load_model(path)
    return model

def predict (model, query):
    return model.predict(query)

