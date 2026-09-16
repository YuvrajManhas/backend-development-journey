import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout = 10)

    response.raise_for_status()

    data = response.json()


    print("Name:", data["name"])
    print("Username:", data["username"])
    print("Email:", data["email"])

    print("City:", data["address"]["city"])
    print("Company:", data["company"]["name"])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

except requests.exceptions.Timeout:
    print("Request Timed Out!")