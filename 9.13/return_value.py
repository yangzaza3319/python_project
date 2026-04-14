# 返回值示例代码

# 1. 无返回值的函数（返回None）
def hello():
    print("123456")
result = hello() # 调用函数
print(f"无返回值函数的返回值是{result}")  # 输出：无返回值函数的返回值是None

# 2. 单返回值的函数 
def single_result(n1):
    return n1 ** 2
n2 = 6
square = single_result(n2)
print(f"{n2}的平方是{square}")  # 输出 ：6的平方是36

# 3. 多返回值的函数

def get_user_info():
    name = "张三丰"
    sex = "男"
    age = 80
    city = "武当"
    return name,sex,age,city
user_name,user_sex,user_age = get_user_info()
print(f"用户信息：{user_name},{user_sex},{user_age}岁")
user_info = get_user_info()
print(f"用户信息（元组接收）:{user_info}")


# 条件返回函数
def check_num(num):
    if num > 0 :
        return "正数"
    elif num < 0 :
        return "负数"
    else :
        return "为0"
print(check_num(5))
print(check_num(-2))
print(check_num(0))
