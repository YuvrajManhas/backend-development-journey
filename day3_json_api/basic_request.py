import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(URL)

print("Response:", response)
print("Status code:", response.status_code)
print("Response Text:", response.text)

