"""
json解析 ---非json格式不能用json解析

"""
import requests
import json

url = "http://127.0.0.1:8000/api/departments/"

num = {
    "data": [
        {
            "dep_id": "T02",
            "dep_name": "Test学院",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
        }
    ]
}

r = requests.post(url, json=num)
# nn = {"ConTent-Type": "application/json"}
# r = requests.post(url, data=json.dumps(num), headers=nn)

print(r.status_code)
print(r.text)
print(r.json())
