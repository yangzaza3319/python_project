# 常用模块3

## random模块
> 用来生成随机数

### 案例1:生成随机数模块
```python
import random

print(random.random())      # 输出 0.687012128698404，打印大于0且小于1之间的小数
print(random.uniform(1,3))  # 输出 1.2471191912922766 大于1小于3的小数

print(random.randint(1,5))       # 输出 大于等于1且小于等于5的随机整数
print(random.randrange(1,10,2))  # 输出 大于等于1且小于10之间的随机奇数

ret = random.choice([1,'23',[4,5]])
print(ret)  # 输出 1或者23或者[4,5]

a,b = random.sample([1,'23',[4,5]],2)
print(a,'和',b) # 列表元素任意两个组合

item = [1,3,5,7,9]
random.shuffle(item)
print(item)   # 输出随机的次序
```
### 案例2:生成随机验证码
```python
import random
import string

def v_code():
    chars = string.ascii_uppercase + string.digits  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' 直接从字符池中随机选字符
    return ''.join(random.choices(chars, k=5))

print(v_code()) # 生成5位的大写数字混合字符
``` 

## OS模块
> 操作系统相应接口

### 工作路径相关
方法|含义
---|---
`os.getcwd()`|获取当前工作目录
`os.chdir("dirname")`|改变当前脚本工作目录
`os.curdir`|返回当前目录`.`
`os.pardir`|获取当前目录的父母录字符串名

### 文件夹相关

方法|含义
---|---
`os.makedirs("dirname1/dirname2")`|可生成多层递归目录
`os.removedirs("dirname1/dirname2")`|若目录为空，则删除，并递归到上级目录，若目录也为空，则删除
`os.mkdir("dirname")`|生成单级目录
`os.rmdir("dirname")`|删除单级空目录，若目录不为空则无法删除（报错）
`os,listdir("dirname")`|列出指定目录下所有文件和子目录

### 文件相关

方法|含义
---|---
`os.remove("文件路径")`|删除一个文件
`os.rename("oldname","newname")`|重命名文件/目录
`os.stat('文件路径')`｜获取文件/目录信息

### 操作系统差异相关

方法|含义
---|---
`os.sep`|输出操作系统特定的路径分隔符
`os.linesep`|输出当前平台使用的行终止符
`os.pathsep`|输出用于分割文件路径的字符串
`os.name`|输出字符串指示当前使用平台

### 执行系统命令相关

方法｜含义
---|---
`os.system(command)`|直接输出执行结果
`os.popen(comand).read()`|获取执行结果
`os.environ`|获取系统环境变量

### 路径相关
方法|含义
---｜---
`os.path.abspath(path)`|返回path规范化的绝对路径
`os.path.split(path)`|将目录分割成目录和文件名二元组返回
`os.path.dirname(path)`|返回path的目录
`os.path.basename(path)`|返回path最后的文件名
`os.path.isdir(path)`|path是一个存在的目录，返回True，否则返回False
`os.path.join(path1[,path2[,...]])`|将多个路径组合后返回，第一个路径之前的参数将被忽略
`os.path.getatime(path)`|返回path所指向的文件或目录的最后访问时间
`os.path.getmtime(path)`|返回path所指向的文件或目录的最后修改时间
`os.path.getsize(path)`|返回path的大小

### 文件属相关

属性|含义
---|---
`st_mode`|inode保护模式
`st_ino`|inode节点号
`st_dev`|inode驻留的设备
`st_nlink`|inode链接数
`st_uid`|所有者的用户ID
`st_gid`|所有者的组ID
`st_size`|普通文件以字节为单位的大小；包含等待某些特殊文件的数据
`st_atime`|上次访问的时间
`st_mtime`|最后一次修改的时间
`st_ctime`|由操作系统报告的“ctime”。在某些系统上（如unix）是最新元数据更改的时间，在其他如Windows系统上是创建时间

## sys模块
> sys模块是与python解释器交互的一个接口

方法|作用
---|---
`sys.argv`|命令行参数List，第一个元素是程序本身的路径
`sys.exit(n)`|退出程序，正常退出返回exit(0),错误退出抛出异常
`sys.version`|获取python程序的版本信息
`sys.path`|返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
`sys.platform`|返回操作系统平台的名称

