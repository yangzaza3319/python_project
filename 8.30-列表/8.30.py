# 定义列表

fruits = ["apple","banana","watermelen"]
print(fruits)  # 输出 ['apple', 'banana', 'watermelen']

# 增加元素
# 1.在索引的位置去增加
fruits.insert(1,"kiwi")

# 2.在最末尾添加
fruits.append("orange")

# 3.用迭代的方法去添加(extend)
## 理解为传递一个List进去，依次添加到末尾
fruits = ["apple","banana","watermelen"]
fruits.extend(['a','b','c'])
print(fruits)  # 输出 ['apple', 'banana', 'watermelen', 'a', 'b', 'c']
fruits = ["apple","banana","watermelen"]
fruits.append(['a','b','c'])
print(fruits) # 输出 ['apple', 'banana', 'watermelen', ['a', 'b', 'c']]


# 删除元素

# 1.删除指定元素
fruits = ["apple","banana","watermelen","orange","apple"]
print(fruits)
fruits.remove("apple") # 仅删除第一个匹配到的元素
print(fruits)
"""
输出 
['apple', 'banana', 'watermelen', 'orange', 'apple']
['banana', 'watermelen', 'orange', 'apple']
"""
# 2.按照索引位置去删除
fruits = ['apple','banana','watermelon','orange','apple']
print(fruits)
res1 =  fruits.pop() # 默认删除最后一个，可以加上索引，有返回值为删除的元素
print(res1)
print(fruits)
res2 = fruits.pop(1)
print(res2)
print(fruits)
""""
输出
['apple', 'banana', 'watermelon', 'orange', 'apple']
apple
['apple', 'banana', 'watermelon', 'orange']
banana
['apple', 'watermelon', 'orange']
"""


# 3.使用切片范围删除
fruits = ['apple','banana','watermelon','orange','berry']
del fruits[0:3]  # 删除索引0,1,2位置的元素，不包含索引3位置的元素
print(fruits)  # 输出 ['orange', 'berry']

# 4.清空列表
fruits = ['apple','banana','watermelon','orange','berry']
fruits.clear()
print(fruits) # 输出 []

# 5.删除列表
fruits = ['apple','watermalen','berry']
print(fruits)
del fruits
print(fruits) # 报错，fruits未定义


# 修改元素
# 1.按照索引修改某个元素的值
city = ["上海", "北京", "悉尼", "巴黎"]
city[2] = "墨尔本"
print(city)  # 输出 ['上海', '北京', '墨尔本', '巴黎']

# 2.切片修改多个元素的值
city = ["上海", "北京", "悉尼", "巴黎"]
city[1:3] = ["东京", "曼谷"]
print(city)  # 输出 ['上海', '东京', '曼谷', '巴黎']


# 查找元素
## 1.对象.index('元素')：返回元素的索引
city = ['北京','上海','杭州','深圳','广州']
print(city.index('上海'))  # 输出 1

## 2.对象.count(element)：返回元素出现的次数
city = ['北京','上海','天津','上海']
print(city.count("上海"))  # 输出 2


# 列表切片
sentence = ['中国','是','个','好地方','好想来','中国']
print(sentence[4:6])  # 输出 [ '好想来', '中国']

# 其他操作
# 1. 对列表进行排序
numbers = [1,3,5,2,4]
numbers.sort()  # 升序
print(numbers)  # 输出 [1, 2, 3, 4, 5]
numbers.sort(reverse=True)  # 降序
print(numbers)  # 输出 [5, 4, 3, 2, 1]
# 2. 反转列表
numbers = [1,3,5,2,4]
numbers.reverse()
print(numbers)  # 输出 [4, 2, 5, 3, 1]
# 3. 获取列表长度
numbers = [1,3,5,2,4]
print(len(numbers))  # 输出 5
# 4. 列表拼接
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)  # 输出 [1, 2, 3, 4, 5, 6]
# 5. 列表重复
list1 = [1,2,3]
list2 = list1 * 3 # 重复3次
print(list2)  # 输出 [1, 2, 3, 1, 2, 3, 1, 2, 3]