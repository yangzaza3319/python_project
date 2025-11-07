# 字典推导式例子
"""
new_dict = {key_expression:value_expression for item in iterable if condition}
"""

#  示例1:生成平方数的字典
square_dict = {x:x ** 2 for x in range(1,10)}
print(square_dict)
# 输出 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 示例2：生成字符及其ascii值的字典

ascii_dict = {char:ord(char) for char in "python"}
print(ascii_dict)
# 输出 {'p': 112, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

# 示例3 将一个字典的key和value对调
example_dict = {'值1':'键1','值2':'键2'}

dict2 = {example_dict[k]:k for k in example_dict}
print(dict2)
# 输出 {'键1': '值1', '键2': '值2'}

# 示例4: 合并(相加)大小写对应的value，将key统一改成小写
dic1 = {'b':1,'a':2,'y':1,'A':4,'Y':9}
dic2 = {k.lower():dic1.get(k.lower(),0)+dic1.get(k.upper(),0) for k in dic1.keys()} 
print(dic2)
""" 输出 
{'b': 1, 'a': 6, 'y': 10}
k.lower()——>所有的键变小写
dic1.get(k.lower(),0)+dic1.get(k.upper(),0)——>k取值的小写大写对应的value相加
"""

## 生成器表达式
gen_expr = (x ** 2 for x in range(5))
print(gen_expr) # 输出 <generator object <genexpr> at 0x101648ee0>
for value in gen_expr:  # 手动迭代
    print(value) 
""" 输出 
0
1
4
9
16
"""

# 综合案例 用一行代码打印出九九乘法表
print(
    '\n'.join(['\t'.join([f'{i}*{j}={i*j}'for j in range(1,i+1)]) for i in range(1,10)])
    )