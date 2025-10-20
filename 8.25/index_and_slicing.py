# 索引与切片

# 索引示例
str1 = "hello python"
print(str1[0])    # 输出：h
print(str1[-1])   # 输出：n


# 切片示例
s = "hello,python~"

## 基本切片
print(s[0:5])    # 输出：hello
print(s[6:12])   # 输出：python

## 步长切片
print(s[::2])  # 输出：hlopto
print(s[::3])  # 输出：hl~

## 省略起始或结束索引
print(s[:5])   # 输出：hello，从开始到索引5（不包含5）
print(s[6:])  # 输出：python~，从索引6到结束

## 反向切片
print(s[::-1])  # 输出：~nohtyp,olleh，字符串反转
print(s[5:0:-1]) # 输出：,olle，从索引5到索引0（不包含0），反向切片
print(s[-7:-1]) # 输出：python从索引-7到索引-1（不包含-1）
