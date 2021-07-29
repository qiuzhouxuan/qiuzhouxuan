# 文件的读写
import json

f = open("1/pytest.text", "rt")
# 读取文件打印全部数据
print(f.read())
# 是否可读
print(f.readable())
# 打印一行数据
print(f.readline())
f.close()
# 优雅的打开文件，自动回收资源，重命名
with open("1/pytest.text", "rt") as q:
    print(q.read())
# json格式转换
json_5 = {
    "name": "luhui000",
    "old": 26,
    "from": "wuh哈an",
}
# JSON转换成字符串
data = json.dumps(json_5, sort_keys=False, indent=4)
print(data)
print(type(data))
# 将json数据转换为字符串写入文件
json.dump(json_5, open("1/pytest.text", "w"))
# 将字符串转换成JSON
str3 = {
    "latitude": 40.000042,
    "longitude": 116.355202,
    "fuelLevel": 59,
    "odometer": 76983,
    "glassBreached": "false",
    "trunkBreached": "false",
    "doorBreached": "false",
    "vehiclePositionChanged": "true",
    "engineStatus": "STARTED",
    "batteryDisconnect": "false",
    "overAccelerationThreshold": "false",
    "vehicleAlarmSystem": "false"
}
print(data)
data = json.loads(str3)
print(type(str3))
