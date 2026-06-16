import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])