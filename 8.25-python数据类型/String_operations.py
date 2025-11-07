# 字符串操作示例

words = "beautiful is better than ugly."

##  字符串的基本操作
print(words)
print(words.capitalize())   # 首字母大写
print(words.swapcase())     # 大小写翻转
print(words.title())        # 每个单词的首字母大写

## 内容居中，宽度为50，填充字符为*
print(words.center(50, '*'))


## 统计子字符串出现的次数
print(words.count("b"))          # 统计 b 出现的次数


## 开头结尾判断
print(words.startswith("b"))     # 判断是否以 b 开头，结果为true
print(words.endswith("y."))      # 判断是否以 y. 结尾，结果为true

## 查找子字符串元素是否存在
print(words.find("is"))          # 查找 is 的索引位置，结果为10
print(words.index("than"))       # 查找 than 的索引位置，结果为20

## 分割字符串，形成列表
### 使用默认分隔符
text = "  Hello   World  Python  \n\t"
print(text.split())  # 输出: ['Hello', 'World', 'Python'] 
                     # 注意: 开头、结尾的空白和中间的多个空格都被忽略了

### 使用一个具体的字符串作为分隔符
# 使用逗号分割
data = "apple banana,cherry,date"
fruits = data.split(',')
print(fruits)  # 输出: ['apple banana', 'cherry', 'date']

# 使用分号分割
items = "one;two;three"
parts = items.split(';')
print(parts)  # 输出: ['one', 'two', 'three']

# 使用特定字符串分割
phrase = "hello-and-hi-there"
parts = phrase.split('-')
print(parts)  # 输出: ['hello', 'and', 'hi', 'there']

# 分隔符不存在于字符串中，输出整个字符串
single = "only_one_word"
result = single.split(',')
print(result)  # 输出: ['only_one_word'] (整个字符串作为一个元素)

### 用maxsplit参数指定分割次数
    # 只分割一次 (maxsplit=1)
url = "https://www.example.com/path/to/page"
protocol_and_rest = url.split("://", 1) # 只分割一次 "://"
print(protocol_and_rest) # 输出: ['https', 'www.example.com/path/to/page']

    # 分割前两次 (maxsplit=2)
sentence = "a-b-c-d-e"
parts = sentence.split('-', 2)
print(parts) # 输出: ['a', 'b', 'c-d-e'] (只分割了前两个 '-', 剩下的 'c-d-e' 作为一个整体)

    # maxsplit=0 表示不分割
no_split = sentence.split('-', 0)
print(no_split) # 输出: ['a-b-c-d-e'] (整个字符串)



# format()方法用法1
name = "yc"
new_name = "吴彦祖"
message1 = "{}的新名字是{}".format(name,new_name) # 输出：yc的新名字是吴彦祖
print(message1)
message2 = "{1}原来的名字是{0}".format("yc","吴彦祖") # 也可以根据索引更改填充顺序 输出：吴彦祖原来的名字是yc
print(message2)

# format()方法用法2:指定关键字的值
str1 = "刀哥"
str2 = "神鹰哥"
str3 = "卢本伟"
sentence = "逆天主播{zhubo1} 、{zhubo2} 、{zhubo3} 都在b站火过一段时间 ".format(
    zhubo1=str1,zhubo2=str2,zhubo3=str3)
print(sentence)  #  输出： 逆天主播刀哥、神鹰哥、卢本伟都在b站火过一段时间

# format()方法用法3：格式化数值
print("圆周率保留两位小数：{:.2f}".format(3.14159265)) # 输出：圆周率保留两位小数：3.14

# format()方法用法4：转化百分比
print("得分：{:.1%}".format(0.856))   # 输出：得分：85.6%

# format()方法用法5:数字千分位
print("金额:{:,}".format(1234567890))  # 输出：金额:1,234,567,890

# format()方法6：对齐
print("|{:<10}|{:^10}|{:>10}|".format("左对齐", "居中", "右对齐")) # 输出：|左对齐       |    居中    |       右对齐|

# format()方法7：填充
print("{:*^10}".format("标题")) # 输出：****标题****

# format()方法8：进制转换
print("255的二进制是：{:b},255的八进制是:{:0},255的十六进制是:{:x}".format(255,255,255)) # 输出：255的二进制是：11111111,255的八进制是:255,255的十六进制是:ff


# format()方法9：转义大括号
print("大括号示例：{{}}".format())  # 输出：{}

# f-string()方法
name = "Alice"
age = 25
print(f"我叫 {name}，今年 {age} 岁")


# strip()、lstrip()、rstrip()方法
xx = '****asdasdasd********'
print(xx.strip('*'))   # 输出：asdasdasd
print(xx.lstrip('*'))  # 输出：asdasdasd********
print(xx.rstrip('*'))  # 输出：****asdasdasd


# 字符替换操作
words = "beautiful is better than ugly."
print(words.replace('e', 'a', 2)) # 输出：baautiful is batter than ugly.


# 字符串类型检查
print(words.isalnum())  # 判断字符串是否只由字母或数字组成
print(words.isalpha())   # 判断字符串是否只由字母组成
print(words.isdigit())   # 判断字符串是否只由数字组成