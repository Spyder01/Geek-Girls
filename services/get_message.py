from .text_processing import prepare_column, extract_keywords, transform, get_description
from .Predict import get_model, predict



def get_message(query):
    # convrt query to lower case:
    query = query.lower()

    keywords = prepare_column('./datasets/Weights.csv')
    keywords_found = extract_keywords(query, keywords)
    if len (keywords_found) == 0:
        return ["I don't know what you mean", ""]
    
    if len (keywords_found) <= 2:
        return ["Insufficient information about symptoms to predict a diagnosis", ""]
    transformed_keywords = transform(keywords_found)
    print (keywords_found)
    model = get_model('./model.pkl')
    prediction = predict(model, transformed_keywords)
    description = get_description(prediction[0])

    return [form_message (prediction[0], "symptom"), form_message (description, "description")]



def form_message (keyword, msg_type):
    if msg_type == "symptom":
        return f"It seems like you have {keyword}"

    if msg_type == "description":
        return f"According to our database, {keyword}"

