import requests

GET_URL = "http://localhost:8000/bag/"

response = requests.get(GET_URL)
data = response.json()
print(data)
