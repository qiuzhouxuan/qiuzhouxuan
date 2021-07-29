import time


def qiu(a):
    # print(a)
    # print(b)
    print(a)


print(qiu(1))
a = lambda x, y: x * y
print(a(5, 8))
list_2 = [1, 2.2, 5, 9, 2, 74, 5, 4, 5, 75, 4]
list_2.append(1)
print(list_2)
list_2.insert(0, 100)
print(list_2)
list_3 = [i ** 2 for i in range(1, 4) if i != 1]
print(list_3)
a = {1, 2, 3, 4}
b = {2, 3, 5, 6, 7, 8, 9, 0}
# 求两个集合的并集
print(a.union(b))
# 求两个集合的交集
print(a.intersection(b))
# 求两个集合的差集
print(a.difference(b))
# 集合添加元素
a.add("dsadas")
print(a)
# 集合去重
b = "yyyyyyyyrewqrweqryieuwyhfishaijfdhsa"
print(set(b))
# 字典键、值取值
json2 = {
    "EventID": "TheftAlarmData",
    "Version": "1.0",
    "Timestamp": 3,
    "Data": {
        "latitude": 40.000042,
        "longitude": 116.355202,
        "fuelLevel": 59,
        "odometer": 76983,
    }}
print(json2.keys())
print(json2.values())
# 字典新建键值
a = {}
b = a.fromkeys((1, 2, 3, 4, 5, 6, 7, 8), "a")
print(b)
# 字典推导式
print({i: i ** 5 for i in range(1, 9)})
print(time.time())
# 格式化输出
a = "hahahaa"
print("我的名字叫做{}".format(a))
a = [1, 2, 3, 4, 5, 6]
print("现在的数字是{}.{},{},{},{},{}".format(*a))
a = {"name": "name", "age": 19}
print("我的名字叫{name}，我的年龄是{age}".format(**a))
