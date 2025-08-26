import requests

url = "http://localhost:9696/subscription"

client = {"job": "student", "duration": 280, "poutcome": "failure"}
response = requests.post(url, json=client).json()

print(response)