# 导包
import requests

url = "http://www.baidu.com"
# get请求
r = requests.get(url)
# 打印 状态码，响应数据，网址
print('r', r.status_code)
print('r', r.text)
print('r', r.url)
print('*' * 50 )
par = {'id': '1001'}
w = requests.get(url, params=par)
print('w', w.status_code)
print('w', w.text)
print('w', w.url)
print('*' * 50 )
pa = {'id': '1001', 'name': "1002"}
x = requests.get(url, params=pa)
print('x', x.status_code)
print('x', x.text)
print('x', x.url)
