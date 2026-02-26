import requests

result = requests.get("http://localhost:8000/api-view-class/")
print(result)

result = requests.post("http://localhost:8000/api-view-class/")
print(result)

result = requests.put("http://localhost:8000/api-view-class/")
print(result)

result = requests.patch("http://localhost:8000/api-view-class/")
print(result)

result = requests.delete("http://localhost:8000/api-view-class/")
print(result.status_code)
