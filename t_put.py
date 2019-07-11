import requests
# import json

url = "http://127.0.0.1:8000/api/departments/T01/"

num = {
    "data": [
        {
            "dep_id": "T01",
            "dep_name": "Test学院-UPDATE",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
        }
    ]
}

r = requests.put(url, json=num)
# nn = {"ConTent-Type": "application/json"}
# r = requests.post(url, data=json.dumps(num), headers=nn)

print(r.status_code)
print(r.text)
