import pandas as pd
from joblib import load

labels = ["Gender_Female", "Gender_Male", "Student_No", "Student_Yes",
        "Married_No", "Married_Yes", "Ethnicity_African American",
        "Ethnicity_Asian", "Ethnicity_Caucasian"]

model = load("model/LimitEstimator.pkl")

def create_df(**kwargs):
    columns = ["Income", "Rating", "Cards", "Age", "Education", "Balance",
        "Gender_Male", "Student_Yes", "Married_Yes",
        "Ethnicity_Asian", "Ethnicity_Caucasian"]

    new_row = {col: [0] for col in columns}  # Initialize all columns to 0
    for key, val in kwargs.items():
        new_row[key] = [val]
    df = pd.DataFrame(new_row)
    return df
