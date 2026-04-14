## 推导式2
### 字典推导式
语法
`new_dict = {键表达式: 值表达式 for 循环变量 in 可迭代对象 if 条件表达式}`
### 示例1
> 生成1-9的平方数字典
```python
square_dict = {x:x ** 2 for x in range(1,10)}
print(square_dict)
```
### 示例2
> 生成字符及其ascii值的字典
```python
ascii_dict = {char:ord(char) for char in "python"}
print(ascii_dict)
```

### 案例1
> 将一个字典的key和value对调
```python
example_dict = {'值1':'键1','值2':'键2'}
dict2 = {example_dict[k]:k for k in example_dict}
print(dict2)
```

### 案例2
> 合并大小写对应的value，将key统一改成小写

## 生成器表达式
> 把列表推导式的`[]`换成`()`就变成了生成器表达式，相比于列表表达式，生成器表达式*不会直接产生值，而是需要我们手动去迭代它*
### 生成器表达式案例
```python
gen_expr = (x ** 2 for x in range(5))
print(gen_expr) # 输出 <generator object <genexpr> at 0x101648ee0>
for value in gen_expr:  # 手动迭代
    print(value) 
```

## 推导式综合案例：用一行代码打印出九九乘法表
```python
print(
    '\n'.join(['\t'.join([f'{x}*{y}={x*y}' for x in range(y+1)]) for y in range(1,10)])
    )
```