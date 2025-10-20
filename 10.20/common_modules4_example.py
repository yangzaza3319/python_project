# 单字符匹配
import re

print(re.findall(r'\w','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['s', '大', 's', 'a', 'j', 'a', 'd', 'h', '1', '2', '3', 'f', 'g', '_']
print(re.findall(r'\W','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['^', ')', '(', ' ', '\t', ' ', '\n', ')'] 除`\w`匹配内容以外的字符

print(re.findall(r'\s','s大sajadh123fg^)(_ \t \n)'))  # 输出 [' ', '\t', ' ', '\n'] 等空白符
print(re.findall(r'\S','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['s', '大', 's', 'a', 'j', 'a', 'd', 'h', '1', '2', '3', 'f', 'g', '^', ')', '(', '_', ')']等非空白符

print(re.findall(r'\d','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['1', '2', '3'] 等纯数字
print(re.findall(r'\D','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['s', '大', 's', 'a', 'j', 'a', 'd', 'h', 'f', 'g', '^', ')', '(', '_', ' ', '\t', ' ', '\n', ')']等非纯数字

print(re.findall(r'\As大','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['s大'] 
print(re.findall(r'\As大sajadh123','s大sajadh123fg^)(_ \t \n)')) # 输出 ['s大sajadh123']
print(re.findall(r'\Amm','s大sajadh123fg^)(_ \t \n)'))    # 输出 [] 字符串不是以 "mm" 开头，因此无匹配（注：原注释说输出 [''] 是错误的，实际为 []）

print(re.findall(r'87..\Z','s大sajadh123fg^)(_ \t \n)usa87..'))      # 输出 ['87..']
print(re.findall(r'\Z..','s大sajadh123fg^)(_ \t \n)usa87..'))      # 输出 [] \Z 表示字符串结尾位置，其后无法再匹配任何字符

print(re.findall(r'\n','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['\n']
print(re.findall(r'\t','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['\t']

print(re.findall(r'^s','s大sajadh123fg^)(_ \t \n)'))    # 输出 ['s']
print(re.findall(r'^s.*','s大sajadh123fg^)(_ \t \n)'))  # 输出 ['s大sajadh123fg^)(_ \t '] 以 's' 开头并匹配到换行符前的所有内容（`.` 不匹配 `\n`）

print(re.findall(r'123\n','s大sajadh123fg^)(_ \t \n)'))  # 输出 [] 因为 '123' 后是 'f'，并非换行符，故无匹配

print(re.findall(r'.','s大sajadh123fg^)(_ \t \n)'))      # 输出除换行符 `\n` 外的所有单个字符组成的列表（`.` 默认不匹配 `\n`）

print(re.findall(r'','s大sajadh123fg^)(_ \t \n)'))       # 输出 22 个空字符串 `''`，因空模式在长度为 21 的字符串中有 22 个匹配位置（包括首尾间隙）


# 重复匹配

import re

print(re.findall('a.b','ab aab a*b a2b a爱b a\nb'))  
"""
输出 ['aab', 'a*b', 'a2b', 'a爱b']
不加`re.DOTALL`的话默认忽略形如`\n \t`等处理多行文字的转义符
"""
print(re.findall('a.b','ab aab a*b a2b a爱b a\nb',re.DOTALL)) 
"""
输出 ['aab', 'a*b', 'a2b', 'a爱b', 'a\nb']
加上`re.DOTALL`匹配形如`\n \t`等处理多行文字的转义符
"""

print(re.findall('a?b','ab aab abb aaaab a爱b aba**b'))  # 输出 ['ab', 'ab', 'ab', 'b', 'ab', 'b', 'ab', 'b']  ，匹配一个b，前面可以有0个或多个a
print(re.findall('a+b','ab aab aaab abbb bcd'))  # 输出 ['ab', 'aab', 'aaab', 'ab']，匹配符号左边含有a的字符

print(re.findall('a*b','ab aab aaab abbb'))   # 输出 ['ab', 'aab', 'aaab', 'ab', 'b', 'b'] ，匹配符号左侧有0个或多个a，右侧有一个b的字符
print(re.findall('ab*','ab aab aaab abbbb cd ')) # 输出 ['ab', 'a', 'ab', 'a', 'a', 'ab', 'abbbb']，匹配符号左侧有0或多个ab的字符

print(re.findall('a{2,4}b','ab abc aab aaab aaaab abbbb '))  # 输出 ['aab', 'aaab', 'aaaab']，匹配2～4个左侧字符

print(re.findall('a.*b','ab  a1b  aaaaaab a*()b'))  # 输出 ['ab  a1b  aaaaaab a*()b']
print(re.findall('a.*?b','ab  a1b  aaaaaab a*()b')) # 输出 ['ab', 'a1b', 'aaaaaab', 'a*()b']

print(re.findall('a[abc]b','aabcd bcda 123 aab ccb abb a_b dacb')) # 输出 ['aab', 'aab', 'abb', 'acb']

print(re.findall('a[0-9]b','a1b a3b aab a*b a_b'))      # 输出 ['a1b', 'a3b']
print(re.findall('a[a-z]b','akb a1b akkb amb a6b'))     # 输出 ['akb', 'amb']
print(re.findall('a[a-zA-Z]b','a1b akb amb a4b anb'))   # 输出 ['akb', 'amb', 'anb']
print(re.findall('a[0-9][0-9]b','a11b a12b a86b a*b arb a_b')) # 输出 ['a11b', 'a12b', 'a86b']
print(re.findall('a[*-+]b','a-b a*b a+b a/b a6b'))      # 输出 ['a*b', 'a+b']

print(re.findall('a[^a-z]b','acb adb a3b a*b'))   # 输出 ['a3b', 'a*b']

print(re.findall('(.*?)_66','python6666 cs_66 一二_66 nice_66'))
"""
输出 ['python6666 cs', ' 一二', ' nice'] 
按照分组规则，匹配到_66之后向前回溯找到最短的匹配
"""
print(re.findall('href="(.*?)"','<a href="https://www.baidu.com">点击</a>')) # 输出 ['https://www.baidu.com']

print(re.findall('compan(y|ies)','Too many companies have gone bankrupt,and the next one is her company'))
"""
输出 ['ies', 'y']
只匹配`()`内的内容
"""
print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt,and the next one is her company'))
"""
输出 ['companies', 'company']
将整体匹配出来
"""

# 常用方法案例
import re

print(re.findall('a','aghqiidnqwdqodjqdq')) # findall 全部找到并返回一个列表

print(re.search('China',"I love China and welcome to repulic The People's Republic of China")) # 输出 ['China', 'China']
print(re.search(r'(\w+) China', "I love China and welcome to republic The People's Republic of China").group(1)) # 输出 love

print(re.match('xiaowenhao','xiaowen 66 66 demon '))  # match 从字符串的起始位置开始匹配，起始位置不满足模式，则直接返回None
print(re.match('xiaowenhao','xiaowenhao 66 66 demon ').group())

print(re.split('[:：,;；;,]','1;3,c,a：5'))  # 按照任意分隔符进行分割 输出 ['1', '3', 'c', 'a', '5']

print(re.sub('小问号','小句号','欢迎小问号来中国')) # 输出 欢迎小句号来中国


# 根据包含的正则表达式的字符串创建模式对象。可以实现更有效率的匹配
obj = re.compile('\d{2}')
print(obj.search('abc123eeee').group()) # 输出 12
print(obj.findall('1231232aasd'))       # 输出 ['12', '31', '23']

# finditer返回一个存放匹配结果的迭代器

ret = re.finditer('\d','asd123affes32432')
print(ret)                         # 输出 <callable_iterator object at 0x1008b4190>
print(next(ret).group())           # 输出 1
print([i.group() for i in ret])    # 输出 ['2', '3', '3', '2', '4', '3', '2']

# 命名分组举例
import re

# 为分组命名，通过分组名获取对应值
ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
print(ret.group('tag_name'))      # 输出 h1
print(ret.group())                # 输出 <h1>hello</h1>

# 使用序号替换命名，通过分组序号获取对应值
ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
print(ret.group(1))              # 输出 h1
print(ret.group())               # 输出 <h1>hello</h1>

# shutil模块：拷贝内容

import shutil
import os

# 创建测试文件和目录
os.makedirs('test_dir/subdir', exist_ok=True)
with open('source.txt', 'w') as f:
    f.write('Hello World!\nThis is a test file.')

try:
    # 1. 拷贝文件内容到新文件
    with open('source.txt', 'r') as src, open('content_copy.txt', 'w') as dst:
        shutil.copyfileobj(src, dst)
    
    # 2. 完整拷贝文件（包括内容）
    shutil.copyfile('source.txt', 'file_copy.txt')
    
    # 3. 拷贝文件及所有元数据（权限、时间等）
    shutil.copy2('source.txt', 'full_copy.txt')
    
    # 4. 拷贝整个目录树
    shutil.copytree('test_dir', 'backup_dir', dirs_exist_ok=True)
    
    # 5. 移动文件
    shutil.move('content_copy.txt', 'test_dir/moved_file.txt')
    
    # 6. 创建压缩档案
    shutil.make_archive('backup', 'zip', 'test_dir')
    
    print("所有操作完成！")
    
    # 7. 清理：删除创建的文件和目录
    os.remove('source.txt')
    os.remove('file_copy.txt') 
    os.remove('full_copy.txt')
    os.remove('backup.zip')
    shutil.rmtree('test_dir')
    shutil.rmtree('backup_dir')
    
except Exception as e:
    print(f"错误: {e}")


# 压缩案例（zipfile）
import zipfile

import zipfile
import os

# 创建测试文件
with open('a.txt', 'w') as f:
    f.write('文件A内容')
with open('b.txt', 'w') as f:
    f.write('文件B内容')

# 压缩文件
with zipfile.ZipFile('ab.zip', 'w') as z:
    z.write('a.txt')
    z.write('b.txt')
    print(f"压缩完成，文件列表: {z.namelist()}")

# 解压到指定目录
extract_path = os.path.expanduser('~/Desktop/extracted')
os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile('ab.zip', 'r') as z:
    z.extractall(path=extract_path)
    print(f"解压到: {extract_path}")

# 查看压缩包信息
with zipfile.ZipFile('ab.zip', 'r') as z:
    for info in z.infolist():
        print(f"文件: {info.filename}, 大小: {info.file_size} bytes")

# 清理
os.remove('a.txt')
os.remove('b.txt')
os.remove('ab.zip')


# 压缩案例（tarfile）
import tarfile
import os

# 创建测试文件和目录
os.makedirs('test_files', exist_ok=True)
with open('test_files/a.py', 'w') as f:
    f.write('print("文件A")')
with open('test_files/b.py', 'w') as f:
    f.write('print("文件B")')

# 压缩文件
with tarfile.open('example.tar', 'w') as t:
    t.add('test_files/a.py', arcname='a.bak')
    t.add('test_files/b.py', arcname='b.bak')
    print("压缩完成")

# 查看压缩包内容
with tarfile.open('example.tar', 'r') as t:
    print(f"压缩包内容: {t.getnames()}")

# 解压缩到指定目录
extract_path = 'extracted'
os.makedirs(extract_path, exist_ok=True)

with tarfile.open('example.tar', 'r') as t:
    t.extractall(extract_path)
    print(f"解压到: {extract_path}")

# 压缩为 gzip 格式
with tarfile.open('example.tar.gz', 'w:gz') as t:
    t.add('test_files/a.py', arcname='a.bak')
    t.add('test_files/b.py', arcname='b.bak')
    print("gzip压缩完成")

# 清理
import shutil
shutil.rmtree('test_files')
shutil.rmtree('extracted')
os.remove('example.tar')
os.remove('example.tar.gz')
