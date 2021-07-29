# 读取yaml文件
import yaml

# load是把yaml格式转换程字典和列表
y = yaml.load(open("demo.yml"), Loader=yaml.FullLoader)
print(type(y))
print(y)
# 文件中-代表列表、
# 字典直接写为 a:1
# dump将字典或者列表转换程yaml格式
print(yaml.dump({'a': [1, 2]}))
# 将字典写入yml文件
with open("demo2.yml", "w") as f:
    yaml.dump(data={"a": [1, 2]}, stream=f)
