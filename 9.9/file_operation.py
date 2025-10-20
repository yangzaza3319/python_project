# 文件操作
import os

print("Current working directory:", os.getcwd()) # 确认当前工作路径

file = open('SRE-Study/python/9.9/example.txt','r')

content = file.read()
print(content)
line = file.readline()
print(line,"+++++")
lines = file.readlines()
print(lines,"----")

"""
输出
Current working directory: /Users/jeyng/Desktop/Git_Root
这是一个用来演示文件操作的的文件
+
这是一行文字
这是第二行文字
 +++++
[] ----
"""

# 指针操作
"""通过操作指针来使readline()和readlines()有内容读取"""
file = open('SRE-Study/python/9.9/example.txt','r')

content = file.read()
print(content)
file.seek(0)
line = file.readline()
print(line,"+++++")
file.seek(0)
lines = file.readlines()
print(lines,"----")
"""
这是一个用来演示文件操作的的文件

这是一行文字
这是第二行文字
这是一个用来演示文件操作的的文件 # readline()方法仅读取第一行(即指针所在行)
+++++
['这是一个用来演示文件操作的的文件\n', '\n', '这是一行文字\n', '这是第二行文字'] ----   # 返回一个列表(无格式) 
"""

# 通过while循环按行读取文件内容
file1 = open("SRE-Study/python/9.9/example.txt")
i = 1
while True:
    text1 = file1.readline().strip()    # 通过strip()方法移除字符串开头和结尾的空白字符
    if text1:
        print("这是第%s行内容⬇️" %i)
        i += 1
        print(text1)
    else :
        break
file1.close()

# 通过for循环遍历按行读取文件所有内容
file2 = open("SRE-Study/python/9.9/example.txt")
for i in file2.readlines():
    print(i.strip())

file2.close()

# 写入内容
file = open('diary.txt','a',encoding='utf-8')
content = input("请输入新加入的内容\n")
file.write(content+"\n")
print("日记已经保存")

file.close()
"""
输出

请输入新加入的内容
请输入新加入的内容
请输入新加入的内容
请输入新加入的内容
123
日记已经保存
"""

# with 结构
with open('diary.txt','r') as file:
    content = file.read()
print(content)

# with结构写简单的备份程序
## 执行下面代码之前记得先创建文件`a.txt`和`b.txt`
source = 'a.txt'
dest = 'b.txt'
with open(source,'r',encoding='utf-8') as src:
    content = src.read()
with open(dest,'w',encoding='utf-8') as dest:
    dest.write(content)
print(f"备份成功!'{source}'的内容已经备份到'{dest}!'")
"""
打开项目根目录会发现一毛一样内容的a.txt和b.txt
"""