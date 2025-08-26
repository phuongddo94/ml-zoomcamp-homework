import pickle

with open("dv.bin", "rb") as f:
    dv = pickle.load(f)

with open("model1.bin", "rb") as f:
    model = pickle.load(f)

customer = {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print(y_pred)