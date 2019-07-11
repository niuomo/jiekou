"""content--字节码"""

import requests

url = "http://www.baidu.com"

r = requests.get(url)

print(r.content)