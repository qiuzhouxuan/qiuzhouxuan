import requests

r = requests.get("https://www.baidu.com")
print(r)
# 设置编码格式
r.encoding = "utf-8"
print(r.text)
# 获取二进制的响应内容
print(r.content)
