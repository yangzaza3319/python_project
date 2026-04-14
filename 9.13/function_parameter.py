# 函数的参数

## 形参 实参
def greet01(name):
    print(f"hello,{name}！")
greet01("吴彦祖")  # 输出 hello,吴彦祖！
greet01("刘亦菲")  # 输出 hello,刘亦菲！


## 位置参数

def greet02(name,age):
    print(f"个人信息：1.姓名{name}  2.年龄{age}")
greet02("yc",18)           # 输出 个人信息：1.姓名yc  2.年龄18

## 默认参数、关键字参数、可选参数

def greet03(name,site="https://www.ujs.edu.cn/",address="学府路301号"):
    print(f"site:{site},address:{address}")

greet03(address="解放路438号",name="北固校区",site="www.baidu.com")  
 # 输出  site:www.baidu.com,address:解放路438号


# 动态参数
## *args 允许函数接受任意数量的位置参数，这些参数会被收集到一个元组中。
def sum_numbers(*args):
    total = sum(args) # args 是一个元组
    return total
result = sum_numbers(1,2,3,4,5) # 可以传入任意数量的参数
print(result)  # 输出 15


## **kwargs 允许函数接受任意数量的关键字参数，并且这些参数会被收集到一个字典
def print_info(**kwargs):
   for key,value in kwargs.items():
      print(f"{key}:{value}") 

print_info(姓名="王多余",年龄=10,城市="西红柿") 
# 输出
    #   姓名:王多余
    #   年龄:10
    #   城市:西红柿
