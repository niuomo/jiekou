"""headers用法 1查看响应信息头"""
import requests

url = "http://www.baidu.com"

r = requests.get(url)
# 查看信息头---输出形式为字典---可以通过键名查看值
print(r.headers)
print("")
print('*' * 50)
