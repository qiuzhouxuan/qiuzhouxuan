# str3 =  """{
# 		"latitude": 40.000042,
# 		"longitude": 116.355202,
# 		"fuelLevel": 59,
# 		"odometer": 76983,
# 		"glassBreached": "false",
# 		"trunkBreached": "false",
# 		"doorBreached": "false",
# 		"vehiclePositionChanged": "true",
# 		"engineStatus": "STARTED",
# 		"batteryDisconnect": "false",
# 		"overAccelerationThreshold": "false",
# 		"vehicleAlarmSystem": "false"
# }"""
# # 将字符串转换成JSON格式
# print(type(str3))
# print(json.loads(str3))
# # 将json从文件中读取并且转换成JSON格式
# jsobj=json.load(open("1/pytest.text","r"))
# print(jsobj)

# 捕获异常
#
# try:
#     num1 = int(input("请输入一个除数"))
#     num2 = int(input("请输入一个被除数"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("被除数不能为零")
# except ValueError:
#     print("输入类型不为数字")
# # 有异常才执行excrpt代码块，不管是否有异常都会执行else代码块
# else:
#     print("**********完成运算*********")
# # 没有异常时会执行finally这块代码
# finally:
#     print("无论是否有异常都会执行这块代码")
class Person:
    # def __init__(self,name,age,gender):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"name:{self.name},age；{self.age},gender:{self.gender} 我在吃")

    def drink(self):
        print(f"name:{self.name},age；{self.age},gender:{self.gender} 我在喝")

    def run(self):
        print(f"name:{self.name},age；{self.age},gender:{self.gender} 我在跑")


QIUZHOUXUAN = Person("qiuzhouxuan", 10, "fdsa")
print(QIUZHOUXUAN.eat)


class Game:
    hp = 1000
    power = 200

    def filght(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
