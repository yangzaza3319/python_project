# json模块：序列化/反序列化

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


# json模块：文件内容相关
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

# pickle模块基本用法：序列化/反序列化
import pickle

data = {
    'name':'123',
    'age':30,
    'studentRole':['math','english']
}
print(pickle.dumps(data)) # 序列化
print(pickle.loads(pickle.dumps(data))) # 反序列化

# pickle模块基本用法：文件内容相关

import pickle

# Step 1: 生成 data.pkl（序列化）
data = {"message": "Hello, pickle!"}
with open('./data.pkl', 'wb') as f:
    pickle.dump(data, f)
    pickle.dump([10, 20, 30], f)

# Step 2: 反序列化（读取）
print("开始反序列化...")
with open('./data.pkl', 'rb') as f:
    first = pickle.load(f)
    second = pickle.load(f)

print("反序列化成功！")
print("对象1:", first)
print("对象2:", second)

# hash案例1

import hashlib

text = "Hello, hashlib!"
# 方法1：一步到位
sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
print("SHA256:", sha256_hash)  # SHA256: fb7062978814273e670bf8dc43b7f3f83442b95c1f6aaf48c9d72c1d172acdca

# 方法2：分步更新（适合大文件或流式数据）
hash_obj = hashlib.sha256()
hash_obj.update(text.encode('utf-8'))
print("SHA256 (分步):", hash_obj.hexdigest())  # 输出 SHA256 (分步): fb7062978814273e670bf8dc43b7f3f83442b95c1f6aaf48c9d72c1d172acdca

# 对文件计算哈希

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

# 加盐

import pickle
import hashlib
import secrets

## 1. 生成或定义盐（salt）
### 方式1：每次随机生成（适合唯一标识）
salt = secrets.token_bytes(32)  # 32字节随机盐

### 方式2：固定盐（仅用于测试，生产环境不要用固定盐！）
salt = b"my_fixed_salt_2025"

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
hash1 = file_hash('data.pkl')
print("原始SHA:",hash1)                 # 输出 原始SHA: 8401184a7e694962a2fbb1e8592af0d456699647ad76f38f68772d8d7a75d00f
print("data.pkl 已生成")                # 输出 data.pkl 已生成
print("Salt (hex):", salt.hex())       # 输出 Salt (hex): 6d795f66697865645f73616c745f32303235
print("加盐 SHA256:", hashed)           # 输出 加盐 SHA256: 1092aa26ee97eca06054a12d3043e8867c2e584e0cca735335a2f54c6b5266ea


# 密码验证的案例
import hashlib
import os

salt = os.urandom(16)   # 模拟注册：生成16字节盐
password = b"123456"    # 模拟注册：模拟输入用户密码

stored_hash = hashlib.pbkdf2_hmac(
    'sha256',# 等价于 hash_name='sha256',
    password,# 等价于 password=password,
    salt,# 等价于 salt=salt,
    10 # 等价于 iterations=10),表示迭代次数设为10
)
print("这是用户注册完成的提示")


def password_verify(stored_hash,stored_salt,input_password): # 模拟登录操作
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        input_password,
        stored_salt,
        10
        )
    return new_hash == stored_hash
pwd = bytes(input('input passwd:'),encoding='utf-8')

print(password_verify(stored_hash,salt,pwd))   # 用哈希后的pwd 来验证密码