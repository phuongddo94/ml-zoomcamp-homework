import pickle
import os

from flask import Flask, request, jsonify

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    churn = y_pred >= 0.5

    return jsonify({
        'churn_probability': float(y_pred),
        'churn': bool(churn)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)