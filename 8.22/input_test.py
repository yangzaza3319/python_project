name = input("请输入您的姓名：")
print(name)
# ！！通过input()函数输入的内容一律会被当作字符串处理！！
a = input("请输入一个数字：")
print(type(a)) # 输出为str
print(a + "1") # 如果输入5，输出51，而不是6
b = int(input("请输入一个数字：")) # 可以进行强制类型转换来输出需要的类型
print(type(b)) # 输出为int
print(b + 1) # 如果输入5，输出6