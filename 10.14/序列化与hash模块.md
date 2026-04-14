## 序列化相关模块
> 序列化：将原本的字典、列表等内容转换为一个字符串的过程（相反的过程叫反序列化）

> 序列化的目的:
> 1. 以某种存储形式使自定义对象持久化
> 2. 将对象从一个地方传递到另一个地方
> 3. 使程序更具可维护性

### 序列化的结果
Python | Json
--- | ---
`dict`|`object`
`list/tuple`|`array`
`str`|`string`
`int/float`|`number`
`True`|`true`
`False`|`false`
`None`|`null`

#### `json`模块
> `json`模块用于处理JSON数据格式。JSON是一种轻量级的数据交换格式，易于人类阅读和编写，同时也有利于及其解析和生成。它提供了简单的方式来编码（序列化）和解码（反序列化）`JSON`数据

##### 常用功能
1. 序列化：将python数据类型转换为json格式
2. 反序列化：将json格式的数据转换为python数据类型

##### 基本用法

1. 序列化&反序列化
```python

import json
data = {
    "name":"小问号",
    "age" : 18,
    "studentRole": False,
    "courses":["SRE","Python"]
}

json_string = json.dumps(data) # 将Python对象转换为json字符串
print(json_string)             # 输出 {"name": "\u5c0f\u95ee\u53f7", "age": 18, "studentRole": false, "courses": ["SRE", "Python"]}

data = json.loads(json_string) # 将Python对象转换为json字符串
print(data)                    # {'name': '小问号', 'age': 18, 'studentRole': False, 'courses': ['SRE', 'Python']}
print(data['name'])            # 输出 小问号，访问字典中`name`键对应的值

```

2. 文件内容相关
```python
import json

## 第一步：创建并写入 json_data.json
initial_data = {
    "name": "alice",
    "age": 22,
    "studentRole": True,
    "courses": ["math", "physics"]
}

with open('json_data.json', 'w', encoding='utf-8') as file:
    json.dump(initial_data, file, indent=4)

print(" 文件 'json_data.json' 已创建并写入数据。")

## 第二步：从刚刚创建的文件中读取数据
with open('json_data.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

print("从文件中读取的数据：")
print(loaded_data)
```
##### 序列化相关参数
参数|作用
---｜---
`skipkeys`| 用于对字典的键进行类型检查，默认为False，当字典的键不是JSON归案支持的基本类型时，直接抛出`TypeError`异常，反之跳过这的键，不引发错误，但会导致数据丢失 
`indent`| 控制json字符串的格式化缩进，默认值None会生成最紧凑的JSON字符串，无缩进和多余空格
`ensure_ascii`| 控制非ASSCII字符转义行为，默认为True,中文会被转义为unicode转义序列
`separators`| 自定义json字符串元素间的分隔符和减值对的分隔符
`sotr_keys`| 是否将数据根据key排序


#### `pickle`模块
> Python的pickle模块用于对象的序列化（将对象转换为字节流）和反序列化（将字节流转换回对象）。这使得在程序之间传递对象或将对象保存到文件中更加方便
> 和json模块不同的是，pickle模块序列化出来的内容只有python认识，其他编程语言识别为乱码。（json序列化出来的是通用格式，即普通字符串，其他编程语言都认识）

##### 基本用法
1. 序列化/反序列化
```python
import pickle

data = {
    'name':'123',
    'age':30,
    'studentRole':['math','english']
}
print(pickle.dumps(data)) # 序列化
print(pickle.loads(pickle.dumps(data))) # 反序列化
```

#### `shelve`模块
> shelve模块允许将python对象存储在文件中，以便在后续的程序运行中重新加载，类似于字典
基本用法
```python
import shelve
shelf = shelve.open('my_shelf') # 打开文件
shelf['name'] = '小问号'
shelf['age'] = 30
shelf['courses'] = ['math','science']

print(shelf['name']) # 读取数据
shelf['age'] = 11 # 更新数据
del shelf['courses'] # 删除数据
shelf.close() # 关闭文件
```

#### `hashlib` 模块
> 密码加密（存储哈希值而非明文）
> 文件完整性校验（如下载文件后验证 SHA256）
> 生成唯一标识（如缓存键）
1. 哈希算法（又叫做摘要算法、散列算法）
它通过一个函数，把任意长度的数据转换为一个固定长度的数据串（通常用16进制的字符串表示）
2. 摘要算法
通过摘要函数对任意长度的数据计算出固定长度的摘要，目的是为了发现原始数据是否被人篡改过
摘要算法之所以能够指出数据是否被篡改过，是因为摘要函数是一个单向函数，计算摘要很容易，但要通过摘要反推数据却非常困难。对原始数据做一个字节的修改，都会导致计算出来的摘要完全不同

`hashlib`支持多种哈希算法
包括：MD5、SHA-1、SHA-224、SHA-256、SHA-384、SHA-512、BLAKE-2

##### 基本用法
1. 对字符串计算哈希

```python
import hashlib

text = "Hello, hashlib!"
# 方法1：一步到位
sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
print("SHA256:", sha256_hash)

# 方法2：分步更新（适合大文件或流式数据）
hash_obj = hashlib.sha256()
hash_obj.update(text.encode('utf-8'))
print("SHA256 (分步):", hash_obj.hexdigest())
# 
```

2. 对文件计算哈希

```python

import pickle
import hashlib

# === 第一步：生成 data.pkl ===
data = {"name": "Alice", "score": 95}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
    pickle.dump([1, 2, 3, 4, 5], f)

print(" data.pkl 已生成")                              # 输出  data.pkl 已生成

# === 第二步：计算文件的 SHA256 哈希 ===
def file_hash(filepath, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

sha256 = file_hash('data.pkl')
print(f" 文件 data.pkl 的 SHA256 哈希值为:\n{sha256}")  # 输出 18bf9deb06ca6247e95c6fb2ffc95c81c13dd4e12801a48956c469f6ca345147
```

##### 加盐
> 用于哈希来保护敏感数据（如密码）时需要加盐

```python
import pickle
import hashlib
import secrets

# 1. 生成或定义盐（salt）
# 方式1：每次随机生成（适合唯一标识）
salt = secrets.token_bytes(32)  # 32字节随机盐

# 方式2：固定盐（仅用于测试，生产环境不要用固定盐！）
# salt = b"my_fixed_salt_2025"

# 2. 生成 data.pkl
data = {"user": "Alice", "role": "admin"}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
    pickle.dump([1, 2, 3], f)

# 3. 计算“加盐哈希”：salt + 文件内容
def salted_file_hash(filepath, salt):
    hash_obj = hashlib.sha256()
    hash_obj.update(salt)  # 先加盐
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# 4. 计算并保存盐和哈希（实际应用中盐需安全存储）
hashed = salted_file_hash('data.pkl', salt)

print("data.pkl 已生成")
print("Salt (hex):", salt.hex())
print("加盐 SHA256:", hashed)
```
##### 哈希函数注意事项
- 不可逆性：哈希函数是不可逆的，意味着无法从哈希值恢复原始数据
- 碰撞: 不同的输入可能产生相同的哈希值
- 安全性：对于密码存储，需要用更安全的哈希算法和适当的盐值来增强安全性

##### 使用场景

- 用于验证文件或数据在传输过程中未被篡改
- 将用户密码的哈希值存在数据库中，而不是明文密码
- 用于创建数字签名，确保数据来源的可靠性

##### 案例：密码验证
 见相应的配套案例文件