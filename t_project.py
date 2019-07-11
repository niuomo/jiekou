"""小项目
登录post---我的订单
用cookies
"""
import requests

# 获取cookies
url_cookies = "http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.7398774078691166"

r = requests.get(url_cookies)
cookies = {"PHPSESSID": r.cookies.get("PHPSESSID")}
print("*" * 50)
# 带cookies登录
url_login = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.0"
data = {"username": "13831499999", "password": "123456", "verify_code": "8888"}
r = requests.post(url_login, data=data, cookies=cookies)
# 带cookies点击我的订单 --用cookies证明我登录成功了
url_order = "http://127.0.0.1/Home/Order/order_list.html"
w = requests.get(url_order, cookies=cookies)
# 打印信息
print(w.text)

