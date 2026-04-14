# 字典
## 字典的定义
dic = {"name":'cs',"age":'18',"job":'IT'}
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': 'IT'}
print("名字是"+dic["name"]) # 输出 名字是cs
print("年龄是"+dic["age"]) # 输出 年龄是18
print("工作是"+dic["job"]) # 输出 工作是IT

## 字典的增删改查
## 通过键值对来增加
dic["兴趣爱好"]="打羽毛球"
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': 'IT', '兴趣爱好': '打羽毛球'}
dic["job"]="后端开发" # 若键存在，则直接对其原来的值进行修改
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}

## 删除键值
dic = {'name': "张三", 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
### 1.删除指定的键
name = dic.pop("兴趣爱好","查无此项") # 删除指定的键，并返回该键对应的值
print(name) # 输出 打羽毛球
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': '后端开发'}
name = dic.pop("兴趣爱好") # 删除指定的键，但该键不存在时会报错
print(name) # 报错 KeyError: '兴趣爱好'
name = dic.pop("兴趣爱好","查无此项") # 异常处理，如果键不存在,输出后面的内容
print(name) # 输出 查无此项

### 2.用del属性删除指定键值对
dic = {'name': "张三", 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
print(dic) # 输出 {'name': '张三', 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
del dic['name']
print(dic) # 输出 {'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}

### 3.删除最后插入的键值对
dic = {'name': "张三", 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
print(dic) # 输出 {'name': '张三', 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
item = dic.popitem() # 删除最后插入的键值对，并返回该键值对
print(item) # 输出 ('兴趣爱好', '打羽毛球')
print(dic) # 输出 {'name': '张三', 'age': '18', 'job': '后端开发'}

### 4.使用clear属性清空字典
dic = {'name': "张三", 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
print(dic) # 输出 {'name': '张三', 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
dic.clear() # 清空字典
print(dic) # 输出 {}

## 修改键值
dic = {'name': "张三", 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
print(dic) # 输出 {'name': '张三', 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
dic["job"]="运维开发" # 直接通过键来修改对应的值，不支持批量修改
print(dic) # 输出 {'name': '张三', 'age': '18', 'job': '运维开发', '兴趣爱好': '打羽毛球'}
dic.update({"name":"李四","age":"20",'job':"前端开发"}) # 通过update属性来批量修改键值对
print(dic) # 输出 {'name': '李四', 'age': '20', 'job': '前端开发', '兴趣爱好': '打羽毛球'}

## 查找键值
### 1. 直接通过键名获取，键名不存在会报错
dic = {'name':"小问号",'学院':"计算机学院","专业":"物联网工程"}
print(dic) # 输出 {'name': '小问号', '学院': '计算机学院', '专业': '物联网工程'}
print(dic['专业'])
### 2.使用get方法获取键值，不存在则返回None，可以自定义返回值
dic = {'name':"小问号",'学院':"计算机学院","专业":"物联网工程"}
print(dic.get("学院")) # 输出 计算机学院
print(dic.get('age')) # 输出 None
print(dic.get('id',"无此信息")) # 输出 无此信息

### 3. IN关键字，存在返回True，反之False
dic = {'name':"小问号",'学院':"计算机学院","专业":"物联网工程"}
print("age" in dic) # 输出 False

## 其他操作
### 1.对键和值进行迭代操作
dic = {'name':"张三",'age':"18","备注":"一个学霸"}
for i in dic.items():
    print(i) 
    """
    将键和值以元组列出
    输出 
    ('name', '张三')
    ('age', '18')
    ('备注', '一个学霸')
    """
for i in dic:
    print(i)
    """
    只迭代键
    输出
    name
    age
    备注
    """

### 2. 使用keys()和values()方法获取键值
dic = {'name':"张三",'age':"18","备注":"一个学霸"}
print(dic.keys(),type(dic.keys())) # 输出 dict_keys(['name', 'age', '备注']) <class 'dict_keys'>
print(dic.values(),type(dic.values())) # 输出 dict_values(['张三', '18', '一个学霸']) <class 'dict_values'>