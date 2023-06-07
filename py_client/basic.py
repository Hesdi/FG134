import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"title": "Main page"}) #HTTP Request
print(get_response.json())
# print(get_response.status_code)