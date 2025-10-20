## 内置函数 
### 作用域相关内置函数
1. `locals()`
    以字典的类型返回当前位置的全部局部变量
2. `globals()`
    以字典的类型返回全部全局变量
    
#### 示例
```python

a = 1
b = 2

print(locals())
print(globals())

def fun(argv):
    c = 2
    print(locals())
    print(globals())

func(3)

```
### 字符串类型处理函数
#### 1. eval()
> 将传入的字符串当作 Python 表达式进行解析和执行，并返回表达式的结果
```python
result = eval('2 + 3')
print(result) # 输出5

n = -2
result = eval('n + 3')
print(result) # 输出1

eval('print("hello world")') # 输出 hello world
```

#### 2. exec()函数
> 作用和eval()函数类似，但是返回值为空
```python
str = '''
for i in range(5):
    print(i)
'''
exec(str)
```

#### 3. compile()
> 用于将源代码编译成字节码，从而可以在后续执行中使用
主要作用——> 将字符串形式的代码转换为可以通过exec()或eval()执行的代码对象
- 语法
```python
compile(source,filename,mode,flags=0,dont_inherit=False,optimize=-1)
```
- 参数
    source：要编译的源代码，可以是字符串或AST(抽象语法树)对象
    filename：表示代码的文件名（通常为字符串），用于错误消息的显示。可以是任意字符串
    mode：指定编译模式
        1. exec ——> 用于编译多条语句（如模块或函数）
        2. eval ——> 用于编译单个表达式
        3. single ——> 用于编译单个交互式语句
- 返回值
返回一个代码对象，可以用exec或eval执行

- 示例
    - 流程语句使用exec
    ```python
    code1 = 'for i in range(5):print(i)'
    compile1 = compile(code1,'','exec')
    exec(compile1)
    ```
    - 简单求值表达式用eval
    ```python
    code2 = '1+2+3'
    compile2 = compile(code2,'',eval)
    eval(compile2)
    ```
    - 交互语句用single
    ```python
    code3 = 'name = input("please input your name: ")'
    compiles3 = compile(code3,'','single')

    exec(compiles3)
    print(name)
    ```