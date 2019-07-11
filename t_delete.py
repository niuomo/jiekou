import requests


url = "http://127.0.0.1:8000/api/departments/T01/"


r = requests.delete(url)


print(r.status_code)
# 删除无响应信息 只有状态码204
