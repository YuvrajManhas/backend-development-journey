import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "Learning APIs",
    "body" : "I am learning JSON and Python requests",
    "userId" : 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())