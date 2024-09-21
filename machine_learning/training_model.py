# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    # Example data
    data = {'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]}
    df = pd.DataFrame(data)

    model = LinearRegression()
    model.fit(df[['X']], df['Y'])

    # Save the model
    joblib.dump(model, 'model.pkl')

train_model()
