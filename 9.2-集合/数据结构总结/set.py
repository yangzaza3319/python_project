# 集合的定义
set1 = { 1,2,3,"章","若","楠" }
set2 = set({1,2,3})

print(set1,set2) # 输出 {1, 2, 3, '楠', '若', '章'} {1, 2, 3}


# 增加元素
# 1. add()属性为集合增加元素
set1 = {1,2,3,'a','b','c'}
print(set1) # 输出 {1, 2, 3, 'b', 'a', 'c'}
set1.add('d')
print(set1) # 输出 {1, 2, 3, 'b', 'd', 'a', 'c'}
print(set1)

# 2. update()属性迭代增加
set = {'yy','b','x','996','1','2','3'}
print(set) # 输出 {'x', 'b', '2', '3', '1', '996', 'yy'}
set.update('e','f')
print(set) # 输出 {'b', '3', 'e', '1', '996', 'yy', 'x', '2', 'f'}
set.update([4,5,6]) # 添加可迭代的数据类型列表[4,5,6],直接按照整个数据结构的格式插入
print(set) # 输出 {'b', 4, 5, 6, '3', 'e', '1', '996', 'yy', 'x', '2', 'f'}

# 删除元素
set = {9,8,7,'d','k','m'}
print(set) # 输出 {'m', 'd', 7, 8, 9, 'k'}
# 1. 使用remove()方法删除元素
set.remove('d')
print(set) # 输出 {'m', 7, 8, 9, 'k'}
# 2. 随机删除某个元素 
set.pop()
print(set) # 输出 {7, 8, 9, 'k'}
# 3. 删除集合
del set
print(set) # 输出 <class 'set'> ，为删除数据的格式

# 查找元素（检查元素是否存在）
set = {0,3,1,9,"up up"}
print("a" in set)   # 输出 False

# 集合的关系
# 1. 取交集(&/intersection方法)
set1 = {1,3,5,"a","c","m"}
set2 = {1,2,3,"j","k",'m'}
print(set1 & set2) # 取交集法1 输出{1, 'm', 3}
print(set1.intersection(set2)) # 取交集法2 输出{1, 'm', 3}

# 2. 取交反集(^/symmetric_difference方法)
set1 = {1,3,5,"a","c","m"}
set2 = {1,2,3,"j","k",'m'}
print(set1 ^ set2)   # 输出 {2, 5, 'a', 'k', 'j', 'c'}
print(set1.symmetric_difference(set2))  # 输出 {2, 5, 'a', 'k', 'j', 'c'}

# 3. 并集(|/union方法)
# > 合并两个集合的元素
set1 = {1,3,5,"a","c","m"}
set2 = {1,2,3,"j","k",'m'}
print(set1|set2)          # 输出 {1, 2, 3, 5, 'a', 'k', 'j', 'm', 'c'}
print(set1.union(set2))   # 输出 {1, 2, 3, 5, 'a', 'k', 'j', 'm', 'c'}

# 4. 差集(-/difference方法)
# > 第一个集合去除两者共有的元素
set1 = {1,3,5,"a","c","m"}
set2 = {1,2,3,"j","k",'m'}
print(set1-set2)             # 输出 {'c', 'a', 5}
print(set1.difference(set2)) # 输出 {'c', 'a', 5}

# 5. 子集与超集(issubset子集/issuperset超集)
# > 当一个集合的元素全部都在另一个集合里，则这个集合是另一个集合的子集，另一个集合是这个集合的超集
## 子集
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}

res1 = set1 < set2
res2 = set1.issubset(set2)

if res1 and res2:  # 两者都为 True
    print("set1 是 set2 的真子集")
else:
    print("set1 不是 set2 的子集")  # 输出 set1 是 set2 的子集

## 超集
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}

res1 = set1 > set2
res2 = set1.issuperset(set2)
if res1 and res2:  # 两者都为 True
    print("set1 是 set2 的超集")
else:
    print("set1 不是 set2 的超集")  # 输出 set1 不是 set2 的超集


# 不可变集合(frozenset()方法创建集合)
## 1. 直接创建一个不可变集合

fs = frozenset([1, 2, 3, 'a', 'b'])
print(fs)  # frozenset({1, 2, 3, 'a', 'b'})

## 2. 通过set来创建

s = {1, 2, 3}
fs = frozenset(s)
print(fs)  # frozenset({1, 2, 3})

# 3.  对集合做修改操作

fs = frozenset([1, 2, 3])

fs.add(4)        # 报错！AttributeError: 'frozenset' object has no attribute 'add'
fs.remove(1)     # 报错！
fs.pop()         # 报错！