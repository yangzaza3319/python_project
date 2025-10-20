# 进阶案例1：基于9.10日案例3。为其增加注册功能并且让整个代码更加合理
db = {}
with open('user.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    for i in data:
        r = i.strip().split('|')
        db[r[0]] = r[1]

while True:
    username = input("请输入你的用户名: ")
    if username in db:
        passwd = input("请输入你的密码: ")
        if passwd == db[username]:
            print("登录成功！")
            break
        else:
            print("密码输入错误！请检查账号或密码")
    else:
        print("账号未创建")
        with open('user.txt','a',encoding='utf-8') as f:
            add = input("请输入你的账号密码，格式为'账号|密码': ")
            f.write(add)
        parts = add.strip().split('|') #  从 add 中提取账号密码，加入 db
        db[parts[0]] = parts[1]
        print("新用户已创建，可立即登录！")

"""
    输出

请输入你的用户名: 112233
账号未创建
请输入你的账号密码，格式为'账号|密码': 112233|112233
13
新用户已创建，可立即登录！
请输入你的用户名: 112233
请输入你的密码: 445566
密码输入错误！请检查账号或密码
请输入你的用户名: 112233
请输入你的密码: 112233
登录成功！
>>> 
"""

# 进阶案例2:同一用户输错3次密码封号（删除账号）
db = {}
with open('user.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    for i in data:
        r = i.strip().split('|')
        db[r[0]] = r[1]
insert_sum = {}
while True:
    
    username = input("请输入你的用户名: ")
    if username in db:
        passwd = input("请输入你的密码: ")
        if passwd == db[username]:
            print("登录成功！")
            break
        else:
            insert_sum[username] = insert_sum.get(username, 0) + 1
            if insert_sum.get(username, 0) <= 2:  # 当前用户输错少于3次
                print("密码输入错误！请检查账号或密码")
            else:
                del db[username]  # 从内存中删除
                with open('user.txt', 'r', encoding='utf-8') as f:  # 从文件中删除：读出所有行，重新写入（去掉该用户）
                    lines = f.readlines() 
                with open('user.txt', 'w', encoding='utf-8') as f:
                    for line in lines:
                        if not line.strip().startswith(username + '|'):
                            f.write(line)
                print("连续输错三次，已为您删除用户")
            
    else:
        print("账号未创建")
        with open('user.txt','a',encoding='utf-8') as f:
            add = input("请输入你的账号密码，格式为'账号|密码': ")
            f.write(add + '\n')
        parts = add.strip().split('|') #  从 add 中提取账号密码，加入 db
        db[parts[0]] = parts[1]
        print("新用户已创建，可立即登录！")

"""
   输出
请输入你的用户名: aaa
账号未创建
请输入你的账号密码，格式为'账号|密码': aaa|123
8
新用户已创建，可立即登录！
请输入你的用户名: aaa
请输入你的密码: 111
密码输入错误！请检查账号或密码
请输入你的用户名: aaa
请输入你的密码: 111
密码输入错误！请检查账号或密码
请输入你的用户名: aaa
请输入你的密码: 111
31
连续输错三次，已为您删除用户
请输入你的用户名: aaa
账号未创建
请输入你的账号密码，格式为'账号|密码': aaa|123
8
新用户已创建，可立即登录！
请输入你的用户名: aaa
请输入你的密码: 123
登录成功！

"""