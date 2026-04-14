# 元组的定义与使用
tuple = (1,2,3,'a','b','c')
print(tuple)
print(tuple[1])

tuple.pop() # 报错，元组无法使用pop属性来修改内容


# 可变元组
tuple = ('1','2','3',[1,4,7])
print(tuple) # 输出 ('1', '2', '3', [1, 4, 7])
tuple[3][2] = 30
print(tuple) # 输出 ('1', '2', '3', [1, 4, 30])
