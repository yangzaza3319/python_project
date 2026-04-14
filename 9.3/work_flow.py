# 判断语句
## 单分支判断
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年了，可以去上网了")
    print("欢迎来到jeyng网吧")
"""
请输入你的年龄：21
你已经成年了，可以去上网了
欢迎来到jeyng网吧
"""

## 双分支判断
age = int(input("请输入你的年龄："))
if age < 18:
    print("您还未成年，人生刚刚开始！")
elif age>18 and age<30:
    print("您的未来充满不确定性，加油少年～")
else :
    print("东隅已逝，桑榆非晚")
"""
请输入你的年龄：19
您的未来充满不确定性，加油少年～

请输入你的年龄：66
东隅已逝，桑榆非晚
"""
## 多分支判断
age = int(input("请输入你的年龄："))
if age < 18:
    print("您还未成年，人生刚刚开始！")
elif age>18 and age<30:
    print("您的未来充满不确定性，加油少年～")
else :
    print("东隅已逝，桑榆非晚")
"""
请输入你的年龄：19
您的未来充满不确定性，加油少年～

请输入你的年龄：16
您还未成年，人生刚刚开始！

请输入你的年龄：66
东隅已逝，桑榆非晚
""" 

# 循环语句
## while循环
### 示例：猜数字小游戏
print("猜数字开始！")
number = 32
while(1):
    guess = int(input("请输入你猜的数字（0-100）"))
    if guess < number:
        print("你猜小啦")
        continue  # 加上continue使得循环从头开始，即重新开始循环
    elif guess > number:
        print("你猜大啦")
        continue
    break         # 两个判断语句均不满足，则结束循环

print("你猜对了！！！")
"""
猜数字开始！
请输入你猜的数字（0-100）1
你猜小啦
请输入你猜的数字（0-100）11
你猜小啦
请输入你猜的数字（0-100）123
你猜大啦
请输入你猜的数字（0-100）32
你猜对了！！！
"""

# while else
## 输入一个数字，判断是否为素数
i = 2
# num = int(input("请输入一个数字，判断它是否为素数"))
# while num > i:
#     if num % i == 0:
#         print(f"{num}不是素数，因为可以被{i}整除")
#         break
#     i  += 1;
# else :
#     print(f"{num}是一个素数")
num = 10
i = 2

while i < num:
    if num % i == 0:
        print(f"{num} 不是素数，因为它可以被 {i} 整除。")
        break
    i += 1
else:
    print(f"{num} 是一个素数！")


# for循环遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

"""
输出
apple
banana
cherry
"""

# 遍历字符串
words = "wuyanzu"
for i in words:
    print(i)

"""
输出 
w
u
y
a
n
z
u
"""
