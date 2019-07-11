"""
post新增
两种数据传入方式 1date--文本 需要将json格式数据转换为文本和添加信息头
                2json --直接传入
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

# r = requests.post(url, json=num)
nn = {"ConTent-Type": "application/json"}
r = requests.post(url, data=json.dumps(num), headers=nn)

print(r.status_code)
print(r.text)
