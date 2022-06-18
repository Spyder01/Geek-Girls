import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

# Function to extract certain keywords from a string
def extract_keywords(query, keywords):
    # Initialize an empty list to store the keywords
    keywords_found = []
    # Loop through the keywords
    for keyword in keywords:
        if validate_string(query, keyword.replace("_", " ")):
            keywords_found.append(keyword)

    # Return the list of keywords
    return keywords_found


def get_weight(keyword):
    dict = get_weight_dictionary('./datasets/Weights.csv')
    return str(dict[keyword])


def transform(keywords):
    transformed_keywords = []
    for keyword in keywords:
        transformed_keywords.append(get_weight(
            keyword.lower().replace(" ", "_")))

    if (len(transformed_keywords) != 17):
        while len(transformed_keywords) != 17:
            transformed_keywords.append("0")

    return np.array(transformed_keywords).reshape(1, -1)


def prepare_column(path):
    symptoms = pd.read_csv(path)
    print(symptoms.head())
    keywords = np.array(symptoms.drop("weight", axis=1)).flatten()
    return keywords


def get_weight_dictionary(path):
    symptoms = pd.read_csv(path)
    print(symptoms.head())
    X = np.array(symptoms.drop("weight", axis=1)).flatten()
    Y = np.array(symptoms["weight"]).flatten()
    dict = {}
    for index in range(len(X)):
        dict[X[index]] = Y[index]
    return dict


def validate_string (query, keyword): 

    # all possible substrings of query
    substrings = [query[i:j+1] for i in range(len(query)) for j in range(i, len(query))]

    for string in substrings: 
        if fuzz.ratio(string, keyword) > 80:
            return True
    
    return False

def get_description (disease):
    descriptions = pd.read_csv ('./datasets/Description.csv')
    return descriptions[descriptions["Disease"] == disease]["Description"].values[0]