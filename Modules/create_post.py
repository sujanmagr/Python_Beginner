import requests

url="https://jsonplaceholder.typicode.com/posts"

payload= {
    "userId": 1,
    "title": "first post",
    "body": "This is my posts"
  }

response=requests.patch(url, json=payload)
print(response.status_code)
print(response.json())
