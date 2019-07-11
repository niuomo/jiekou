"""小项目
登录post---我的订单
用session带过cookies --同一个session 自动记录-发送cookies信息
用session对象进行发送一系列请求
"""
import requests

# 创建session对象  类似约  driver = webdriver.浏览器() 后面直接调用driver即可
sess = requests.session()
url_cookies = "http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.7398774078691166"
# 用session对象调用 获取验证码
sess.get(url_cookies)
print("*" * 50)
# 用session对象--调用登录
url_login = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.0"
data = {"username": "13831499999", "password": "123456", "verify_code": "8888"}
sess.post(url_login, data=data)
# 用session打开我的订单
url_order = "http://127.0.0.1/Home/Order/order_list.html"
w = sess.get(url_order)
# 打印信息
print(w.text)
# 关闭session
sess.close()
