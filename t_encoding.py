"""encoding用法 1查看编码 2设置编码"""
import requests

url = "http://www.baidu.com"

r = requests.get(url)
# 设置编码
r.encoding = "UTF-8"

print('r', r.status_code)
print('r', r.text)
print('r', r.url)
# 查看编码
print("r", r.encoding)
print('*' * 50)
