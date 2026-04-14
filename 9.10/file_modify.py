# 文件修改方法1
import os
with open('a.txt') as read_f,open('a.txt.new','w') as write_f:
    data = read_f.read()
    print(data)
    data = data.replace("这是需要备份的文件","修改方法一：读取全部内容，并统一在内存中修改，最后覆盖到硬盘")  # replace(old,new)
    write_f.write(data)
print(data)
os.remove('a.txt')
os.rename('a.txt.new','a.txt')
"""
输出
这是需要备份的文件
修改方法一：读取全部内容，并统一在内存中修改，最后覆盖到硬盘
"""

import os
with open('a.txt') as read_f, open('a.txt.new', 'w') as write_f:
    for line in read_f:

        print("替换前:", line.rstrip('\n'))  # rstrip('\n') 避免换行叠加

        line = line.replace('这是一段文字a', '替换文字1')
        line = line.replace('这是一段文字b', '替换文字2')

        
        print("替换后:", line.rstrip('\n'))
        print()  

        
        write_f.write(line)

os.remove('a.txt')
os.rename('a.txt.new', 'a.txt')


"""
输出
替换前: 这是一段文字a
替换后: 替换文字1

替换前: 这是一段文字b
替换后: 替换文字2
"""


# 案例2:商品信息管理与总价计算
products = [] # 初始化商品列表
# 读取文件并构建商品列表
with open('goods.txt','r',encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 3:
            product = {
                'name' : parts[0],
                'price': int(parts[1]),   # i['key'] —— 用于访问字典（dict）中的值
                'amount': int(parts[2])
            }
            products.append(product)
print("商品列表",products)
total_price = 0
for i in products:
    total_price += i['price'] * i['amount']

print("总价为:",total_price)
"""
输出
商品列表 [{'name': 'apple', 'price': 10, 'amount': 3}, {'name': 'tesla', 'price': 100000, 'amount': 1}, {'name': 'mac', 'price': 3000, 'amount': 2}, {'name': 'lenovo', 'price': 30000, 'amount': 3}, {'name': 'chicken', 'price': 10, 'amount': 3}]
总价为： 196060
"""

# 案例3:基于文件的账号密码判断
db = {}
with open('user.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    print(data)
    for i in data:
        ret = i.strip().split("|") # 以`|`为分隔符
        print(ret)
        db[ret[0]] = ret[1] # 把列表索引为1的值对应到集合的
    print(db)
while True:
    username = input("请输入您的用户名：")
    if username in db:
        passwd = input("请输入你的密码：")
        if passwd == db[username]:
            print("登录成功") 
            break;
        else:
            print("请检查你的密码")
            break
    else:
        print("账号不存在")
    break

"""
输出
请输入您的用户名：李四
请输入你的密码：112233
请检查你的密码

请输入您的用户名：瓜六
账号不存在

请输入您的用户名：张三
请输入你的密码：112233
登录成功
"""