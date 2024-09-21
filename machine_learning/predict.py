# predict.py
import joblib
import matplotlib.pyplot as plt
import io
import base64

def predict_value(input_value):
    model = joblib.load('model.pkl')
    prediction = model.predict([[input_value]])
    return prediction[0]

def generate_graph():
    plt.figure()
    plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], marker='o')
    plt.title("Sample Graph")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64
