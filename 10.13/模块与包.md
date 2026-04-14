## 模块概述
> 模块(module)是一个包含python代码的文件，通常以`.py`结尾；模块可以包含变量、函数、类，甚至其他模块；通过模块，我们可以把代码组织成不同的文件，以便于更好地管理和复用代码
> 模块可以分为以下三类：1.自定义模块（用户自己编写的模块）2.标准库模块（python自带模块如`math()`、`os()`、`sys()`等） 3.第三方模块（其他开发者编写的模块，通常可以通过`pip()`安装）

## 自定义模块
> 开发者自己编写的 Python 文件（.py 文件），其中包含函数、类、变量等，可以被其他 Python 脚本或模块导入和使用，并且可以用`as`为它取别名
### 自定义模块示例1：取别名
```python
# mymodule.py

print("this is my own module...")

def greet(name):
    return f"hello,{name}!"
def add(a,b):
    return a+b
PI = 3.14159


"""
该自定义模块实现了4个基本的功能
1. 打印提示语，可以用于测试模块是否正常执行
2. 封装打招呼的功能
3. 封装两数相加的功能
4. 定义了PI的值

可以在另一个python文件中导入模块
"""
```

```python
# my_module_maindemo1.py

import my_module

print(my_module.PI)
print(my_module.greet("小问号"))
print(my_module.add(3,6))

"""
输出
this is my own module...
3.14159
hello,小问号!
9
"""

import my_module as mm  # 自定义模块起别名
print(mm.greet("小问号"))  # 输出 hello,小问号!
```

### 自定义模块示例2：根据用户输入导入不同的自定义模块

```python
# mysql.py

def sqlparse():
    print("from mysql sqlparse"+','+"sqlparse是用于语法分析和美化sql代码的模块")
```

```python
def sqlparse():
    print("from oracle sqlparse"+','+"sqlparse是用于语法分析和美化sql代码的模块")
```

```python
# my_module_maindemo2.py

db_type = input("请选择你的数据库类型(mysql/oracle)>>:")

if db_type == 'mysql':
    import mysql as db
elif db_type == 'oracle':
    import oracle as db

db.sqlparse()

"""
输出
请选择你的数据库类型(mysql/oracle)>>:mysql
from mysql sqlparse,sqlparse是用于语法分析和美化sql代码的模块

请选择你的数据库类型(mysql/oracle)>>:oracle
from oracle sqlparse,sqlparse是用于语法分析和美化sql代码的模块
"""
```

### 模块的导入

```python
# 1. 导入多个模块

import sys
import os
import re
# 或者  
import sys,os,re

# 2. 通过from 导入模块
from 文件名 import 功能
from my_module import greet,add

# 3. 覆盖导入模块中的同名函数
def add():
    pass

# 4. 导入除了以下划线`__`开头的所有函数（即python内置的特殊函数）。该导入方法可读性较差且可能造成命名空间污染，一般不推荐
from my_module import *

# 5. 定义`__all__`，显式控制`import *`的输出
## 在需要被导入的模块中定义__all__
__all__ = ['greet','add']
```
#### 全局变量`__name__`
> 用于判断模块是被直接运行，还是被导入

 使用方式|`__name__`的值|说明
---|:---:|:---:
直接运行|`__main__`| 这是程序入口
作为脚本运行|模块名| 模块名

```python
# module_demo.py

def add(a, b):
    return a + b

# 只有直接运行时才执行测试
if __name__ == "__main__":
    print("Testing add function:")
    print(add(2, 3))  # 直接运行`module_demo.py`会输出: 5

# module_demo_main.py


print("准备导入 module_demo 模块...")

import module_demo as md

print(f"导入成功！当前 md.__name__ = {md.__name__}")  # 输出 导入成功！当前 md.__name__ = module_demo

# 调用模块中的函数
result = md.add(10, 20)
print(f"md.add(10, 20) = {result}")

print("测试__name__完成。")
"""

"""
```

### 模块的路径搜索

> python在导入模块时会按照一定的顺序搜索模块所在的位置。主要的搜索路径包括
1. 当前目录：Python首先在当前目录下查找要导入的模块
2. PYTHONPATH环境变量：包含一系列目录名，可以通过设置此变量来添加额外的模块搜索路径
3. 标准库目录：Python安装时自带的标准库所在的目录
4. site-packages目录：第三方模块安装的默认位置

```python
import sys

# 查看当前模块搜索路径
print(sys.path)

# 添加自定义搜索路径
sys.path.append('/.../模块所在目录')

# 在搜索路径开头添加目录(优先级高)
sys.path.insert(0,'/.../模块所在目录')
```
#### 设置PYTHONPATH环境变量

```python
export PYTHONPATH = /.../模块所在目录:$PYTHONPATH # Linux&macOS
set PYTHONPATH = /.../模块所在目录；%PYTHONPATH%
```
> 注意事项
> 1. 不提倡在代码中直接修改`sys.path`,最好通过环境变量或安装包的方式管理模块路径
> 2. 搜索路径的优先级按照`sys.path`列表中的顺序，越靠前优先级越高
> 3. 在导入模块时，一旦在某个路径下找到了对应的模块，就会停止继续搜索

#### 编译python文件
> 为了提高加载模块的速度，python解释器会在`__pycache__`目录下缓存某个模块编译后的版本，格式为：`moudule.version.pyc`,并且会包含python版本号,这种命名规范保证了编译后的结果多版本共存
> 例：在cpython3.3版本下，mymodule.py模块会被缓存成`__pycache/my_module/cpython-33,pyc`

### 包
> python包（Package）是一个包含`__init__.py`文件的目录，它用于组织和管理相关的Python模块
包的主要作用是提供一种命名空间的层次结构，使得大型项目中的模块组织更加清晰
在python3中，虽然`__init__.py`文件不是必须的，但为了保持兼容性和明确目录是一个包，建议始终创建这个文件
包可以包含子包和模块，通过包的层次结构可以避免命名冲突，提高代码的可维护性和重用性

#### 包的使用
1. 示例包结构
```txt
glance/                   # 顶级包（根包）
├── __init__.py      # 包初始化文件，使 glance 成为一个 Python 包
├── api/                 # API 子包：存放与接口相关的模块
│   ├── __init__.py      # API 子包的初始化文件
│   ├── policy.py        # 权限策略相关功能
│   └── versions.py      # 版本管理相关功能
├── cmd/                 # 命令行子包：存放命令行工具或管理脚本
│   ├── __init__.py      # 命令行子包的初始化文件
│   └── manage.py        # 主管理命令入口
└── db/                  # 数据库子包：存放数据模型和数据库操作
    ├── __init__.py      # 数据库子包的初始化文件
    └── models.py        # 数据库模型定义
```

2. 文件内容
```python
# policy.py

def get():
    print('from policy.py')

# versions.py

def create_resource(conf):
    print('from version.py:',conf)

# manage.py

def main():
    print('from manage.py')

# models.py

def register_models(engine):
    print('from models.py:',engine)
```

#### 使用import导入包
```python
import glance.db.models
glance.db.models.register_models('mysql')
```
> 由于python的懒加载,只执行被显式导入的模块

导入方式|语法|特点|使用示例
---|---|---|---
导入整个模块|`import module`|需用 module.func()调用|`import os`、`os.getcwd()`
导入包中的子模块|`import package.submodule`|路径必须完整|`import glance.db.models`
导入并重命名|`import module as alias`|简化名称|`import numpy as np`
从模块导入指定成员|`from module import name`|直接使用|name()	`from math import sqrt`
从包导入子模块|`from package import submodule`|常用于包结构|`from glance.cmd import manage`

##### 案例：只导入顶层包，无法访问子模块
```python
main.py

import glance
glance.cmd.main()  # 报错！cmd 未被导入
```

> 解决办法：在`__init__.py`中显式导入子模块

```python
# glance/__init__.py

from . import cmd      # 使 glance.cmd 可用
from . import db       # 使 glance.db 可用


# glance/cmd/__init__.py

from .manage import main  # 使 glance.cmd.main 可直接调用

# main.py
import glance
glance.cmd.main()  # 成功！
```

#### 使用from导入包
> 从包或模块中导入特定的子模块、函数、类或变量。按需导入，减少命名空间污染，调用更简洁

##### 基本语法
```python
from package import submodule
from package.subpackage import module
from package.module import function, Class, variable
```

1. 从包中导入子包

```python
from glance import cmd
cmd.manage.main()  # 需要 cmd/__init__.py 中导入 manage
```
> `glance/__init__.py`中必须有 `from . import cmd`，否则会报错

2. 从子包中导入模块

```python
from glance.cmd import manage
manage.main()  # 直接调用
```
> 不依赖顶层`__init__.py`,因为路径写全了

3. ⭐️从模块中导入具体函数⭐️（最常用）
```python
from glance.db.models import register_models
from glance.api.policy import get

register_models('mysql')
get()
```

4. 一次性导入多个成员

```python
from glance.api import policy, versions
policy.get()
versions.create_resource("conf")
```
```python
from glance.db.models import register_models
from glance.cmd.manage import main
```

5. 导入并重命名
```python
from glance.cmd.manage import main as glance_main
from json import loads as json_loads
```

#### 绝对导入和相对导入
1. 绝对导入
以执行文件的 sys.path 为起始点开始导入。
- 优点：执行文件与被导入的模块中都可以使用
- 缺点：所有导入都是以 sys.path 为起始点,导入麻烦

2. 相对导入
参照当前所在文件的文件夹为起始开始查找，称之为相对导入

- 符号：`.`代表当前所在文件的文件加,`..`代表上一级文件夹,`...`代表上一级的上一级文件夹
- 优点：导入更加简单
- 缺点：只能在导入包中的模块时才能使用
