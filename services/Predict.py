#from tensorflow.keras.models import load_model
import pickle

def get_model (path="models/model.h5"):
    model = pickle.load(open(path, 'rb'))
    print (model)
    return model

def predict (model, query):
    return model.predict(query)

