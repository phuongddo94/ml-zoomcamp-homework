import pickle
from flask import Flask, request, jsonify

with open("dv.bin", "rb") as f:
    dv = pickle.load(f)

with open("model1.bin", "rb") as f:
    model = pickle.load(f)

app = Flask('subscription')

@app.route('/subscription', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    
    return jsonify({'subscription_probability': y_pred})

if __name__ == '__main__':
    app.run(host='localhost', port = 9696)